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
    "http://www.isc.org/downloads/software-support-policy/" \
    "bind-software-status/"
STABLE_BIND_PATTERN = \
    r'^<td>([^\s\xc2]+).*</td>\n<td class="c_sw">'

STABLE_DHCP_URL = \
    "http://www.isc.org/downloads/software-support-policy/" \
    "dhcp-software-status/"
STABLE_DHCP_PATTERN = \
    r'^<td>([^\s\xc2]+).*</td>\n<td class="c_sw">'

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
    r'<a href.*?>CanIt (.*?) '

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

STABLE_SENDMAILANALYZER_URL = "http://sourceforge.net/projects/sa-report/files/"
STABLE_SENDMAILANALYZER_PATTERN = \
    r'<span>Download sendmailanalyzer-(.*?).tar.gz '

STABLE_DJANGO_URL = "https://www.djangoproject.com/download/"
STABLE_DJANGO_PATTERN = \
    r'<p>The latest official version is (.*?).</p>'

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
    "STABLE_DJANGO_URL", "STABLE_DJANGO_PATTERN"
]
