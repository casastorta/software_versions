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
    print (("stunnel:             %s" % (ver.check_stunnel())))
    print (("Pound:               %s" % (ver.check_pound())))
    print (("Linux kernel:        %s" % (ver.check_linux())))
    print (("Varnish:             %s" % (ver.check_varnish())))
    print (("ClamAV:              %s" % (ver.check_clamav())))
    print (("OpenSSH:             %s" % (ver.check_openssh())))
    print (("Dovecot:             %s" % (ver.check_dovecot())))
    print (("MongoDB:             %s" % (ver.check_mongodb())))
    print (("SpamAssassin:        %s" % (ver.check_spamassassin())))
    print (("Consul:              %s" % (ver.check_consul())))
    print (("MIMEDefang:          %s" % (ver.check_mimedefang())))
    print (("Roundcube:           %s" % (ver.check_roundcube())))
    print (("Vagrant:             %s" % (ver.check_vagrant())))
    print (("HAProxy:             %s" % (ver.check_haproxy())))
    print (("Monit:               %s" % (ver.check_monit())))
    print (("WordPress:           %s" % (ver.check_wordpress())))
    print (("Bacula:              %s" % (ver.check_bacula())))
    print (("Redis:               %s" % (ver.check_redis())))
    print (("unbound:             %s" % (ver.check_unbound())))
    print (("SOGo:                %s" % (ver.check_sogo())))
    print (("CouchDB:             %s" % (ver.check_couchdb())))
    print (("ownCloud:            %s" % (ver.check_owncloud())))
    print (("OpenSMTPD:           %s" % (ver.check_opensmtpd())))


def set_include_path():
    include_path = os.path.abspath("./")
    sys.path.append(include_path)


if __name__ == "__main__":
    set_include_path()
    main()
