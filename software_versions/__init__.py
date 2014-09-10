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
    r'<h1>MySQL Community Server (.*?)</h1>'

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
    r'<p>The latest official version is (.*?).</p>'

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
    "STABLE_DOVECOT_URL", "STABLE_DOVECOT_PATTERN"
]
