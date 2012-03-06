#!/usr/bin/env python
'''
Testcase for software versions.
Scenario:
 Check for latest stable software versions
'''

import os
import sys

def main():

    from software import versions as ver

    print ("Sendmail:    %s" % (ver.check_sendmail()))
    print ("ISC BIND:    %s" % (ver.check_bind()))
    print ("Cyrus-IMAPD: %s" % (ver.check_cyrus_imapd()))
    print ("Apache HTTP: %s" % (ver.check_apache_httpd()))
    print ("SQUID:       %s" % (ver.check_squid()))
    print ("CanIt:       %s" % (ver.check_canit()))
    print ("PostgreSQL:  %s" % (ver.check_postgresql()))
    print ("Squirrel:    %s" % (ver.check_squirrelmail()))
    print ("OpenLDAP:    %s" % (ver.check_openldap()))
    print ("PLA:         %s" % (ver.check_phpldapadmin()))
    print ("Postfix:     %s" % (ver.check_postfix()))
    print ("Nginx:       %s" % (ver.check_nginx()))

def set_include_path():
    include_path = os.path.abspath("./include/")
    sys.path.append (include_path)


if __name__ == "__main__":
    set_include_path()
    main()

