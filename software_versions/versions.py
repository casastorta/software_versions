'''
Created on Nov 21, 2011

@author: vkrivoku
'''

import software_versions as sftw
import re
import sys

dopy2 = False

try:
    # Python 3 way
    import urllib.request as client
except ImportError:
    import urllib as client
    dopy2 = True


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

    return (__grep_out_info(url, pattern, multiline=True, only_first=True))


def check_dhcp():
    '''
    Checks ISC DHCP stable version(s) from the website
    '''
    url = sftw.STABLE_DHCP_URL
    pattern = sftw.STABLE_DHCP_PATTERN

    return (__grep_out_info(url, pattern, multiline=True, only_first=True))


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

    return (__grep_out_info(url, pattern, recursive=True))


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

    return (__grep_out_info(url, pattern, only_first=True))


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

    return (__grep_out_info(url, pattern, only_first=True))


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

    return (__grep_out_info(url, pattern, only_first=True))


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

    return (__grep_out_info(url, pattern, multiline=True, only_first=True))


def check_mysql():
    '''
    Checks MySQL Community Server stable version(s) from the website
    '''
    url = sftw.STABLE_MYSQL_URL
    pattern = sftw.STABLE_MYSQL_PATTERN

    return (__grep_out_info(url, pattern, only_first=True))


def check_proftpd():
    '''
    Checks ProFTPD stable version(s) from the website
    '''
    url = sftw.STABLE_PROFTPD_URL
    pattern = sftw.STABLE_PROFTPD_PATTERN

    return (__grep_out_info(url, pattern))


def check_vsftpd():
    '''
    Checks vsftpd stable version(s) from the website
    '''
    url = sftw.STABLE_VSFTPD_URL
    pattern = sftw.STABLE_VSFTPD_PATTERN

    return (__grep_out_info(url, pattern))


def check_sendmailanalyzer():
    '''
    Checks SendmailAnalyzer stable version(s) from the website
    '''
    url = sftw.STABLE_SENDMAILANALYZER_URL
    pattern = sftw.STABLE_SENDMAILANALYZER_PATTERN

    return (__grep_out_info(url, pattern))


def check_django():
    '''
    Checks Django stable version from the website
    '''
    url = sftw.STABLE_DJANGO_URL
    pattern = sftw.STABLE_DJANGO_PATTERN

    return (__grep_out_info(url, pattern))


def check_stunnel():
    '''
    Checks stunnel stable version from the website
    '''
    url = sftw.STABLE_STUNNEL_URL
    pattern = sftw.STABLE_STUNNEL_PATTERN

    return (__grep_out_info(url, pattern, only_first=True))


def check_pound():
    '''
    Checks Pound stable version from the website
    '''
    url = sftw.STABLE_POUND_URL
    pattern = sftw.STABLE_POUND_PATTERN

    return (__grep_out_info(url, pattern))


def check_linux():
    '''
    Checks Linux kernel stable version from the website
    '''
    url = sftw.STABLE_LINUX_URL
    pattern = sftw.STABLE_LINUX_PATTERN

    return (__grep_out_info(url, pattern))


def check_varnish():
    '''
    Checks Varnish stable version from the website
    '''
    url = sftw.STABLE_VARNISH_URL
    pattern = sftw.STABLE_VARNISH_PATTERN

    return (__grep_out_info(url, pattern))


def check_clamav():
    '''
    Checks ClamAV stable version from the website
    '''
    url = sftw.STABLE_CLAMAV_URL
    pattern = sftw.STABLE_CLAMAV_PATTERN

    return (__grep_out_info(url, pattern))


def check_openssh():
    '''
    Checks OpenSSH stable version from the website
    '''
    url = sftw.STABLE_OPENSSH_URL
    pattern = sftw.STABLE_OPENSSH_PATTERN

    return (__grep_out_info(url, pattern))


def check_dovecot():
    '''
    Checks Dovecot stable version from the website
    '''
    url = sftw.STABLE_DOVECOT_URL
    pattern = sftw.STABLE_DOVECOT_PATTERN

    return (__grep_out_info(url, pattern))


def check_mongodb():
    '''
    Checks MongoDB production version from the website
    '''
    url = sftw.STABLE_MONGODB_URL
    pattern = sftw.STABLE_MONGODB_PATTERN

    return (__grep_out_info(url, pattern))


def check_spamassassin():
    '''
    Checks SpamAssassin stable version from the website
    '''
    url = sftw.STABLE_SPAMASSASSIN_URL
    pattern = sftw.STABLE_SPAMASSASSIN_PATTERN

    return (__grep_out_info(url, pattern))


def check_consul():
    '''
    Checks Consul stable version from the website
    '''
    url = sftw.STABLE_CONSUL_URL
    pattern = sftw.STABLE_CONSUL_PATTERN

    return (__grep_out_info(url, pattern))


def __grep_out_info(
    url, pattern, match_number=1, recursive=False, multiline=False,
    only_first=False, greedy=False
):
    '''
    Does the pull-and-grep part in search for requested info
    '''
    content = ''

    try:
        f = client.urlopen(url)
        content = f.read()
        if dopy2 is False:
            content = content.decode("utf-8")
        f.close()
    except:
        print (("***ERR*** Can't pull %s for software version: %s"
              (url, sys.exc_info()[0])))
        return False

    if (recursive is False):
        # We do search for one-time occurence of a string
        flags = re.DOTALL
        if multiline is True:
            flags = re.MULTILINE
        elif greedy is True:
            flags = re.S

        #flags += re.DEBUG

        m = re.findall(pattern, content, flags)

        if (m is not None):
            if (only_first):
                return([m[0]])
            else:
                return(m)

        else:
            print ("***WARN*** Can't locate %s in %s for software version" %
                  (pattern, url))

            return False
    else:
        # We should do recursive

        parts = re.split('\n', content)
        list = []

        for line in parts[:]:
            m = re.search(pattern, line)
            if (m is not None):
                list.append(str(m.group(match_number)).strip())

        if (len(list) == 0):
            return False

        return list

    return False
