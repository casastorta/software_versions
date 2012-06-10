#!/usr/bin/env python

'''
``software`` module contains functionality to parse out
latest software versions from respective vendors' web sites.
'''

STABLE_SENDMAIL_URL = "http://www.sendmail.com/sm/open_source/download/"
STABLE_SENDMAIL_PATTERN = \
    'Sendmail.*<a href="/sm/open_source/download/(.*)">.*</a> is ' \
    'available from'

STABLE_BIND_URL = "http://www.isc.org/software/bind"
STABLE_BIND_PATTERN = \
    '<a href="/software/bind/.*" title="BIND (.*)".*</a>'

STABLE_CYRUS_IMAP_URL = "http://www.cyrusimap.org/"
STABLE_CYRUS_IMAP_PATTERN = \
    '<p>Version: (.*?)</p>'

STABLE_APACHE_URL = "http://httpd.apache.org/download.cgi"
STABLE_APACHE_PATTERN = \
    '\<h1.*?\>Apache HTTP Server (.*?) \(httpd\)\: (.*?) is the latest'

STABLE_SQUID_URL = "http://www.squid-cache.org/Versions/"
STABLE_SQUID_PATTERN = \
    '<tr><td><a href=".*?">.*?</a></td><td>.*?</td><td>(.*?)</td></tr>' \
    '<tr><td><a href=".*?">.*?</a></td><td>.*?</td><td>(.*?)</td></tr>' \
    '<tr><td>'

STABLE_CANIT_URL = "http://roaringpenguin.com/news"
STABLE_CANIT_PATTERN = \
    '<a href.*?>CanIt (.*?) '

STABLE_PSQL_URL = "http://www.postgresql.org/versions.rss"
STABLE_PSQL_PATTERN = \
    '<item><title>(.*?)(\<\/|$)'

STABLE_SQUIRRELMAIL_URL = "http://squirrelmail.org/download.php"
STABLE_SQUIRRELMAIL_PATTERN = \
    '<b>Stable version</b>.*?<b>Version: (.*?)</b><br />'

STABLE_OPENLDAP_URL = "http://www.openldap.org/software/download/"
STABLE_OPENLDAP_PATTERN = \
    'Our latest release.*?of OpenLDAP Software for general use.*?OpenLDAP-' \
    '(.*?) is currently available'

STABLE_PLA_URL = "http://phpldapadmin.sourceforge.net/wiki/index.php/Release"
STABLE_PLA_PATTERN = \
    '<span class="mw-headline" id="phpLDAPadmin_.*?">' \
    'phpLDAPadmin (.*?)</span></h1>'

STABLE_POSTFIX_URL = "http://cdn.postfix.johnriley.me/mirrors/postfix-release/"
STABLE_POSTFIX_PATTERN = \
    '<a href="official/postfix-(.*?).tar.gz">Source code</a>'

STABLE_NGINX_URL = "http://nginx.org/en/download.html"
STABLE_NGINX_PATTERN = \
    'Stable version</h4>.*?<a href="/download/nginx-(.*?).tar.gz">'

STABLE_MYSQL_URL = "http://www.mysql.com/downloads/mysql/"
STABLE_MYSQL_PATTERN = \
    '<h1>MySQL Community Server (.*?)</h1>'

STABLE_PROFTPD_URL = "http://www.proftpd.org/"
STABLE_PROFTPD_PATTERN = \
		'Stable: <strong>(.*?)</strong>'

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
    "STABLE_NGINX_URL", "STABLE_NGINX_PATTERN"
    "STABLE_MYSQL_URL", "STABLE_MYSQL_PATTERN"
    "STABLE_PROFTPD_URL", "STABLE_PROFTPD_PATTERN"
]
