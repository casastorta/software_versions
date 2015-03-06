#!/usr/bin/env python

'''
``software`` module contains functionality to parse out
latest software versions from respective vendors' web sites.
'''

STABLE_SENDMAIL_URL = "http://www.sendmail.com/sm/open_source/download/"
STABLE_SENDMAIL_PATTERN = \
    r'Sendmail.*<a href="/sm/open_source/download/.*">(.*)</a> is ' \
    r'available from'

STABLE_BIND_URL = \
    "https://www.isc.org/downloads/"
STABLE_BIND_PATTERN = \
    r'<tr>\n<td>(\d+.*)</td>\n<td class="c_sw"><a href'

STABLE_DHCP_URL = \
    "https://www.isc.org/downloads/"
STABLE_DHCP_PATTERN = \
    r'<tr>\n<td><span.*>(\d+.*)</span></td>\n<td class="c_sw"'

STABLE_CYRUS_IMAP_URL = "http://www.cyrusimap.org/"
STABLE_CYRUS_IMAP_PATTERN = \
    r'<p>Version: (.*?)</p>'

STABLE_APACHE_URL = "http://httpd.apache.org/download.cgi"
STABLE_APACHE_PATTERN = \
    r'<a href="\#apache.*">(.*?)</a> \(released'

STABLE_SQUID_URL = "http://www.squid-cache.org/Versions/"
STABLE_SQUID_PATTERN = \
    r'<tr><td><a href="v.*?">.*?</a></td><td>.*?</td><td>(.*?)</td></tr>'

STABLE_CANIT_URL = "http://roaringpenguin.com/news"
STABLE_CANIT_PATTERN = \
    r'>Roaring Penguin Software releases CanIt (.*?)<'

STABLE_PSQL_URL = "http://www.postgresql.org/versions.rss"
STABLE_PSQL_PATTERN = \
    r'<item><title>(.*?)(\<\/|$)'

STABLE_SQUIRRELMAIL_URL = "http://squirrelmail.org/download.php"
STABLE_SQUIRRELMAIL_PATTERN = \
    r'<b>Stable version</b>.*?<b>Version: (.*?)</b><br />'

STABLE_OPENLDAP_URL = "http://www.openldap.org/software/download/"
STABLE_OPENLDAP_PATTERN = \
    r'Our latest release.*?of OpenLDAP Software for general use' \
    r'.*?OpenLDAP-(.*?) is currently available'

STABLE_PLA_URL = "http://phpldapadmin.sourceforge.net/wiki/index.php/Release"
STABLE_PLA_PATTERN = \
    r'<span class="mw-headline" id="phpLDAPadmin_.*?">' \
    r'phpLDAPadmin (.*?)</span></h1>'

STABLE_POSTFIX_URL = "http://de.postfix.org/ftpmirror/"
STABLE_POSTFIX_PATTERN = \
    r'<a href="official/postfix-(.*).tar.gz">Source code</a>'

STABLE_NGINX_URL = "http://nginx.org/en/download.html"
STABLE_NGINX_PATTERN = \
    r'Stable version</h4>.*?<a href="/download/nginx-(.*?).tar.gz">'

STABLE_MYSQL_URL = "http://www.mysql.com/downloads/mysql/"
STABLE_MYSQL_PATTERN = \
    r'<h1>MySQL Community Server (.*?)\s</h1>'

STABLE_PROFTPD_URL = "http://www.proftpd.org/"
STABLE_PROFTPD_PATTERN = \
    r'Stable: <strong>(.*?)</strong>'

STABLE_VSFTPD_URL = "https://security.appspot.com/vsftpd.html"
STABLE_VSFTPD_PATTERN = \
    r'<li>vsftpd-(.*?) is released'

STABLE_SENDMAILANALYZER_URL = \
    "http://sourceforge.net/projects/sa-report/files/"
STABLE_SENDMAILANALYZER_PATTERN = \
    r'<span>Download sendmailanalyzer-(.*?).tar.gz '

STABLE_DJANGO_URL = "https://www.djangoproject.com/download/"
STABLE_DJANGO_PATTERN = \
    r'<li>Latest release: <a href=".*?/download/.*?/tarball/">' \
    r'Django-(.*?).tar.gz</a><br>Checksum: <a href=' \
    r'".*?/download/.*?/checksum/">Django-.*?.checksum.txt</a></li>'

STABLE_STUNNEL_URL = "https://www.stunnel.org/downloads.html"
STABLE_STUNNEL_PATTERN = \
    r'<td><a href="downloads/stunnel-.*?.tar.gz">stunnel-(.*?).tar.gz</a></td>'

STABLE_POUND_URL = "http://www.apsis.ch/pound/"
STABLE_POUND_PATTERN = \
    r'Download the latest version <a .*?>Pound-(.*?).tgz</a>'

STABLE_LINUX_URL = "http://www.kernel.org/"
STABLE_LINUX_PATTERN = \
    r'<td id="latest_link">.*?' \
    r'<a href="./pub/linux/kernel/v3.x/linux-.*?.tar.xz">(.*?)</a>'

STABLE_VARNISH_URL = "https://www.varnish-cache.org/releases"
STABLE_VARNISH_PATTERN = \
    r'<h2 class="pane-title">Current supported releases</h2>.*?' \
    r'<a href="/content/varnish-cache-.*?">Varnish Cache (.*?)</a>'

STABLE_CLAMAV_URL = "http://www.clamav.net/download.html"
STABLE_CLAMAV_PATTERN = \
    r'<h3>The latest stable release is <strong>(.*?)</strong></h3>'

STABLE_OPENSSH_URL = "http://www.openssh.com/"
STABLE_OPENSSH_PATTERN = \
    r'<a href="txt/release-.*?">OpenSSH (.*?)</a> released'

STABLE_DOVECOT_URL = "http://www.dovecot.org/download.html"
STABLE_DOVECOT_PATTERN = \
    r'<h3>Stable releases</h3>.*?' \
    r'Download <a href="releases/.*?/dovecot-(.*?).tar.gz">'

STABLE_MONGODB_URL = "http://www.mongodb.org/downloads"
STABLE_MONGODB_PATTERN = \
    r'<h2 class="release-version".*?>Production Release \((.*?)\)'

STABLE_SPAMASSASSIN_URL = "http://spamassassin.apache.org/downloads.cgi"
STABLE_SPAMASSASSIN_PATTERN = \
    r'<a name="Released_version_relversion" id="Released_version_relversion"' \
    r'><h3>Released version, (.*?)</h3>'

STABLE_CONSUL_URL = "http://www.consul.io/downloads.html"
STABLE_CONSUL_PATTERN = \
    r'<h2 class="os-name">Linux</h2>.*?' \
    r'<li><a href="https://dl.bintray.com/mitchellh/consul/' \
    r'(.*?)_linux_386.zip">32-bit</a></li>'

STABLE_MIMEDEFANG_URL = "http://www.mimedefang.org/"
STABLE_MIMEDEFANG_PATTERN = \
    r'<span class="field-content">Release (.*?)</span>'

STABLE_ROUNDCUBE_URL = "http://roundcube.net/download/"
STABLE_ROUNDCUBE_PATTERN = \
    r'<td class="dlversion"><strong>Complete</Strong>: (.*?)</td>'

STABLE_VAGRANT_URL = "http://www.vagrantup.com/downloads.html"
STABLE_VAGRANT_PATTERN = \
    r'<p>.*?Below are all available downloads for the latest version of ' \
    r'Vagrant.*?\((.*?)\)'

STABLE_HAPROXY_URL = "http://www.haproxy.org/#down"
STABLE_HAPROXY_PATTERN = \
    r'<td>.*?-stable</td>.*?' \
    r'<td><a href="/download/.*?/src/haproxy-.*?.tar.gz">(.*?)</a></td>'

STABLE_MONIT_URL = "http://mmonit.com/monit/#download"
STABLE_MONIT_PATTERN = \
    r'<div class="col-sm-8 col-sm-offset-2">.*?' \
    r'<h3>Monit (.*?) Downloads</h3>'

STABLE_WORDPRESS_URL = "https://wordpress.org/download/"
STABLE_WORDPRESS_PATTERN = \
    r'<p class="intro">The latest stable release of WordPress ' \
    r'\(Version (.*?)\)'

STABLE_BACULA_URL = "http://sourceforge.net/projects/bacula/files/bacula/"
STABLE_BACULA_PATTERN = \
    r'<div id="files"><div class="download-bar">Looking for the latest ' \
    r'version\? <strong>.*?' \
    r'<a href="/projects/bacula/files/latest/download\?source=files" ' \
    r'title="/bacula/.*?/bacula-(.*?).tar.gz'

STABLE_REDIS_URL = "http://redis.io/download"
STABLE_REDIS_PATTERN = \
    r'<td>(.*?)</td>.*?' \
    r'<td>Stable</td>'

STABLE_UNBOUND_URL = "http://unbound.net/download.html"
STABLE_UNBOUND_PATTERN = \
    r'<h2>Unbound Downloads</h2>.*?' \
    r'The latest version of unbound \(currently (.*?)\)'

STABLE_SOGO_URL = "http://www.sogo.nu/downloads/backend.html"
STABLE_SOGO_PATTERN = \
    r'<h2>Source Code</h2>.*?' \
    r'id="downbutton">.*?SOGo-(.*?).tar.gz</a><br/>'

STABLE_COUCHDB_URL = "http://couchdb.apache.org/"
STABLE_COUCHDB_PATTERN = \
    r'<div class="wrap download-pane">.*?' \
    r'<h2 class="icon icon-download">Download CouchDB (.*?)</h2>'

STABLE_OWNCLOUD_URL = "https://owncloud.org/install/"
STABLE_OWNCLOUD_PATTERN = \
    r'<h3><strong>Install ownCloud Server</strong>.*?' \
    r'<p>Latest stable version: (.*?)\s\('

STABLE_OPENSMTPD_URL = "https://opensmtpd.org/"
STABLE_OPENSMTPD_PATTERN = \
    r'<a href="/announces/release-.*?.txt">OpenSMTPD (.*?)</a> released'

STABLE_PHP_URL = "http://php.net/"
STABLE_PHP_PATTERN = \
    r"<li><a class='download-link' href='/downloads.php#v.*?'>(.*?)</a>" \
    r"<span class='dot'>&middot;</span><a class='notes' " \
    r"href='/ChangeLog-5.php#.*?'>Release Notes</a></li>"

STABLE_CASSANDRA_URL = "http://cassandra.apache.org"
STABLE_CASSANDRA_PATTERN = \
    r'Latest release <b>(.*?)</b>'

STABLE_COBBLER_URL = "http://www.cobblerd.org/"
STABLE_COBBLER_PATTERN = \
    r'<div class="header">Latest Version:</div>.*?' \
    r'<div class="version">(.*?)</div>'

STABLE_RIAK_URL = "http://docs.basho.com/riak/latest/downloads/"
STABLE_RIAK_PATTERN = \
    r'<h1>Download Riak (.*?)</h1>'

STABLE_PYTHON_URL = "https://www.python.org/downloads/"
STABLE_PYTHON_PATTERN = \
    r'<a class="button" ' \
    r'href="https://www.python.org/ftp/python/.*?/Python-.*?">' \
    r'Download Python (.*?)</a>'

STABLE_RUBY_URL = "https://www.ruby-lang.org/en/downloads/"
STABLE_RUBY_PATTERN = \
    r'<a href="http://cache.ruby-lang.org/pub/ruby/.*?/ruby-.*?.tar.gz">' \
    r'Ruby (.*?)</a>'

STABLE_LXC_URL = "https://linuxcontainers.org/lxc/downloads/"
STABLE_LXC_PATTERN = \
    r'Stable release tarballs are available for download below..*?' \
    r'<a href="/downloads/lxc/lxc-.*?.tar.gz">.*?' \
    r'lxc-(.*?).tar.gz'

__all__ = [
    "STABLE_SENDMAIL_URL", "STABLE_SENDMAIL_PATTERN",
    "STABLE_BIND_URL", "STABLE_BIND_PATTERN",
    "STABLE_CYRUS_IMAP_URL", "STABLE_CYRUS_IMAP_PATTERN",
    "STABLE_APACHE_URL", "STABLE_APACHE_PATTERN",
    "STABLE_SQUID_URL", "STABLE_SQUID_PATTERN",
    "STABLE_CANIT_URL", "STABLE_CANIT_PATTERN",
    "STABLE_PSQL_URL", "STABLE_PSQL_PATTERN",
    "STABLE_SQUIRRELMAIL_URL", "STABLE_SQUIRRELMAIL_PATTERN",
    "STABLE_OPENLDAP_URL", "STABLE_OPENLDAP_PATTERN",
    "STABLE_PLA_URL", "STABLE_PLA_PATTERN",
    "STABLE_POSTFIX_URL", "STABLE_POSTFIX_PATTERN",
    "STABLE_NGINX_URL", "STABLE_NGINX_PATTERN",
    "STABLE_MYSQL_URL", "STABLE_MYSQL_PATTERN",
    "STABLE_PROFTPD_URL", "STABLE_PROFTPD_PATTERN",
    "STABLE_VSFTPD_URL", "STABLE_VSFTPD_PATTERN",
    "STABLE_SENDMAILANALYZER_URL", "STABLE_SENDMAILANALYZER_PATTERN",
    "STABLE_DJANGO_URL", "STABLE_DJANGO_PATTERN",
    "STABLE_STUNNEL_URL", "STABLE_STUNNEL_PATTERN",
    "STABLE_POUND_URL", "STABLE_POUND_PATTERN",
    "STABLE_LINUX_URL", "STABLE_LINUX_PATTERN",
    "STABLE_VARNISH_URL", "STABLE_VARNISH_PATTERN",
    "STABLE_CLAMAV_URL", "STABLE_CLAMAV_PATTERN",
    "STABLE_OPENSSH_URL", "STABLE_OPENSSH_PATTERN",
    "STABLE_DOVECOT_URL", "STABLE_DOVECOT_PATTERN",
    "STABLE_MONGODB_URL", "STABLE_MONGODB_PATTERN",
    "STABLE_SPAMASSASSIN_URL", "STABLE_SPAMASSASSIN_PATTERN",
    "STABLE_CONSUL_URL", "STABLE_CONSUL_PATTERN",
    "STABLE_MIMEDEFANG_URL", "STABLE_MIMEDEFANG_PATTERN",
    "STABLE_VAGRANT_URL", "STABLE_VAGRANT_PATTERN",
    "STABLE_HAPROXY_URL", "STABLE_HAPROXY_PATTERN",
    "STABLE_MONIT_URL", "STABLE_MONIT_PATTERN",
    "STABLE_WORDPRESS_URL", "STABLE_WORDPRESS_PATTERN",
    "STABLE_BACULA_URL", "STABLE_BACULA_PATTERN",
    "STABLE_REDIS_URL", "STABLE_REDIS_PATTERN",
    "STABLE_UNBOUND_URL", "STABLE_UNBOUND_PATTERN",
    "STABLE_SOGO_URL", "STABLE_SOGO_PATTERN",
    "STABLE_COUCHDB_URL", "STABLE_COUCHDB_PATTERN",
    "STABLE_OWNCLOUD_URL", "STABLE_OWNCLOUD_PATTERN",
    "STABLE_OPENSMTPD_URL", "STABLE_OPENSMTPD_PATTERN",
    "STABLE_PHP_URL", "STABLE_PHP_PATTERN",
    "STABLE_CASSANDRA_URL", "STABLE_CASSANDRA_PATTERN",
    "STABLE_COBBLER_URL", "STABLE_COBBLER_PATTERN",
    "STABLE_RIAK_URL", "STABLE_RIAK_PATTERN",
    "STABLE_PYTHON_URL", "STABLE_PYTHON_PATTERN",
    "STABLE_RUBY_URL", "STABLE_RUBY_PATTERN",
    "STABLE_LXC_URL", "STABLE_LXC_PATTERN"
]
