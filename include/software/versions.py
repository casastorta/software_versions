'''
Created on Nov 21, 2011

@author: vkrivoku
'''

from types import NoneType
import software as sftw
import re
import urllib

def check_sendmail():
    '''
    Checks sendmail stable version from the website
    '''
    url = sftw.STABLE_SENDMAIL_URL
    pattern = sftw.STABLE_SENDMAIL_PATTERN

    return (__grep_out_info(url, pattern))


def check_bind():
    '''
    Checks BIND stable version(s) from the website
    '''
    url = sftw.STABLE_BIND_URL
    pattern = sftw.STABLE_BIND_PATTERN

    return (__grep_out_info(url, pattern, recursive=True))


def check_cyrus_imapd():
    '''
    Checks Cyrus-IMAPD stable version(s) from the website
    '''
    url = sftw.STABLE_CYRUS_IMAP_URL
    pattern = sftw.STABLE_CYRUS_IMAP_PATTERN

    return (__grep_out_info(url, pattern))


def check_apache_httpd():
    '''
    Checks Apache HTTPD stable version(s) from the website
    '''
    url = sftw.STABLE_APACHE_URL
    pattern = sftw.STABLE_APACHE_PATTERN

    return (__grep_out_info(url, pattern))


def check_squid():
    '''
    Checks Squid-cache stable version(s) from the website
    '''
    url = sftw.STABLE_SQUID_URL
    pattern = sftw.STABLE_SQUID_PATTERN

    return (__grep_out_info(url, pattern))


def check_canit():
    '''
    Checks CanIt stable version(s) from the website
    '''
    url = sftw.STABLE_CANIT_URL
    pattern = sftw.STABLE_CANIT_PATTERN

    return (__grep_out_info(url, pattern))


def check_postgresql():
    '''
    Checks PostgreSQL stable version(s) from the website
    '''
    url = sftw.STABLE_PSQL_URL
    pattern = sftw.STABLE_PSQL_PATTERN

    return (__grep_out_info(url, pattern, recursive=True))


def check_squirrelmail():
    '''
    Checks Squirrelmail stable version(s) from the website
    '''
    url = sftw.STABLE_SQUIRRELMAIL_URL
    pattern = sftw.STABLE_SQUIRRELMAIL_PATTERN

    return (__grep_out_info(url, pattern))


def check_openldap():
    '''
    Checks OpenLDAP stable version(s) from the website
    '''
    url = sftw.STABLE_OPENLDAP_URL
    pattern = sftw.STABLE_OPENLDAP_PATTERN

    return (__grep_out_info(url, pattern))


def check_phpldapadmin():
    '''
    Checks PLA stable version(s) from the website
    '''
    url = sftw.STABLE_PLA_URL
    pattern = sftw.STABLE_PLA_PATTERN

    return (__grep_out_info(url, pattern))


def check_nginx():
    '''
    Checks Nginx stable version(s) from the website
    '''
    url = sftw.STABLE_NGINX_URL
    pattern = sftw.STABLE_NGINX_PATTERN

    return (__grep_out_info(url, pattern))


def check_postfix():
    '''
    Checks Postfix MTA stable version(s) from the website
    '''
    url = sftw.STABLE_POSTFIX_URL
    pattern = sftw.STABLE_POSTFIX_PATTERN

    return (__grep_out_info(url, pattern))


def __grep_out_info(url, pattern, match_number=1, recursive=False):
    '''
    Does the pull-and-grep part in search for requested info
    '''
    content = ''
    try:
        f = urllib.urlopen(url)
        content = f.read()
    except:
        print ("***ERR*** Can't pull %s for software version" % (url))
        return False

    f.close()

    if (recursive is False):
        # We do search for one-time occurence of a string
        m = re.search(pattern, content, re.DOTALL)

        if (type(m) is not NoneType):
            return [ str(m.group(match_number)).strip() ]

        else:
            print ("***WARN*** Can't locate %s in %s for software version" % \
                (pattern, url))

            return False
    else:
        # We should do recursive

        parts = re.split('\n', content)
        list = []

        for line in parts[:]:
            m = re.search(pattern, line)
            if (type(m) is not NoneType):
                list.append(str(m.group(match_number)).strip())

        if (len(list) == 0):
            return False

        return list

    return False
