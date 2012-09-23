import unittest
import sys
import os


class TestVersionFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test_sendmail(self):
        ver.check_sendmail()

    def test_bind(self):
        ver.check_bind()

    def test_cyrus_imapd(self):
        ver.check_cyrus_imapd()

    def test_apache_httpd(self):
        ver.check_apache_httpd()

    def test_squid(self):
        ver.check_squid()

    def test_canit(self):
        ver.check_canit()

    def test_postgresql(self):
        ver.check_postgresql()

    def test_squirrelmail(self):
        ver.check_squirrelmail()

    def test_openldap(self):
        ver.check_openldap()

    def test_phpldapadmin(self):
        ver.check_phpldapadmin()

    def test_postfix(self):
        ver.check_postfix()

    def test_nginx(self):
        ver.check_nginx()

    def test_mysql(self):
        ver.check_mysql()

    def test_proftpd(self):
        ver.check_proftpd()

    def test_vsftpd(self):
        ver.check_vsftpd()


def set_include_path():
    include_path = os.path.abspath("../include/")
    sys.path.append(include_path)


if __name__ == "__main__":
    set_include_path()
    from software import versions as ver

    unittest.main()
