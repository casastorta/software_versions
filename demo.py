#!/usr/bin/env python
'''
Testcase for software versions.
Scenario:
 Check for latest stable software versions
'''

import os
import sys


def main():

    from software_versions import versions as ver

    print (("Sendmail:            %s" % (ver.check_sendmail())))
    print (("ISC BIND:            %s" % (ver.check_bind())))
    print (("ISC DHCP:            %s" % (ver.check_dhcp())))
    print (("Cyrus-IMAPD:         %s" % (ver.check_cyrus_imapd())))
    print (("Apache HTTP:         %s" % (ver.check_apache_httpd())))
    print (("SQUID:               %s" % (ver.check_squid())))
    print (("CanIt:               %s" % (ver.check_canit())))
    print (("PostgreSQL:          %s" % (ver.check_postgresql())))
    print (("Squirrel:            %s" % (ver.check_squirrelmail())))
    print (("OpenLDAP:            %s" % (ver.check_openldap())))
    print (("PLA:                 %s" % (ver.check_phpldapadmin())))
    print (("Postfix:             %s" % (ver.check_postfix())))
    print (("Nginx:               %s" % (ver.check_nginx())))
    print (("MySQL:               %s" % (ver.check_mysql())))
    print (("ProFTPD:             %s" % (ver.check_proftpd())))
    print (("vsftpd:              %s" % (ver.check_vsftpd())))
    print (("SendmailAnalyzer:    %s" % (ver.check_sendmailanalyzer())))
    print (("Django:              %s" % (ver.check_django())))
    print (("HP 8560p BIOS:       %s" % (ver.check_hpbios())))
    print (("stunnel:             %s" % (ver.check_stunnel())))


def set_include_path():
    include_path = os.path.abspath("./")
    sys.path.append(include_path)


if __name__ == "__main__":
    set_include_path()
    main()
