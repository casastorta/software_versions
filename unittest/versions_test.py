#!/usr/bin/env python

import unittest

import sys
import os
import re


class TestVersionFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test_sendmail(self):
        #if (self.__test_version(ver.check_sendmail()) == False):
        #    self.addError("Sendmail version doesn't seem to be version")
        self.assertTrue(
            self.__test_version(ver.check_sendmail())
        )

    def test_bind(self):
        self.assertTrue(
            self.__test_version(ver.check_bind())
        )

    def test_dhcp(self):
        self.assertTrue(
            self.__test_version(ver.check_dhcp())
        )

    def test_cyrus_imapd(self):
        self.assertTrue(
            self.__test_version(ver.check_cyrus_imapd())
        )

    def test_apache_httpd(self):
        self.assertTrue(
            self.__test_version(ver.check_apache_httpd())
        )

    def test_squid(self):
        self.assertTrue(
            self.__test_version(ver.check_squid())
        )

    def test_canit(self):
        self.assertTrue(
            self.__test_version(ver.check_canit())
        )

    def test_postgresql(self):
        self.assertTrue(
            self.__test_version(ver.check_postgresql())
        )

    def test_squirrelmail(self):
        self.assertTrue(
            self.__test_version(ver.check_squirrelmail())
        )

    def test_openldap(self):
        self.assertTrue(
            self.__test_version(ver.check_openldap())
        )

    def test_phpldapadmin(self):
        self.assertTrue(
            self.__test_version(ver.check_phpldapadmin())
        )

    def test_postfix(self):
        self.assertTrue(
            self.__test_version(ver.check_postfix())
        )

    def test_nginx(self):
        self.assertTrue(
            self.__test_version(ver.check_nginx())
        )

    def test_mysql(self):
        self.assertTrue(
            self.__test_version(ver.check_mysql())
        )

    def test_proftpd(self):
        self.assertTrue(
            self.__test_version(ver.check_proftpd())
        )

    def test_vsftpd(self):
        self.assertTrue(
            self.__test_version(ver.check_vsftpd())
        )

    def test_sendmailanalyzer(self):
        self.assertTrue(
            self.__test_version(ver.check_sendmailanalyzer())
        )

    def test_django(self):
        self.assertTrue(
            self.__test_version(ver.check_django())
        )

    def test_stunnel(self):
        self.assertTrue( \
            self.__test_version(ver.check_stunnel()) \
        )

    def test_pound(self):
        self.assertTrue( \
            self.__test_version(ver.check_pound()) \
        )

    def test_linux(self):
        self.assertTrue( \
            self.__test_version(ver.check_linux()) \
        )

    def test_varnish(self):
        self.assertTrue( \
            self.__test_version(ver.check_varnish()) \
        )

    def test_clamav(self):
        self.assertTrue( \
            self.__test_version(ver.check_clamav()) \
        )

    def test_openssh(self):
        self.assertTrue( \
            self.__test_version(ver.check_openssh()) \
        )

    def test_dovecot(self):
        self.assertTrue( \
            self.__test_version(ver.check_dovecot()) \
        )

    def test_mongodb(self):
        self.assertTrue( \
            self.__test_version(ver.check_mongodb()) \
        )

    def test_spamassassin(self):
        self.assertTrue( \
            self.__test_version(ver.check_spamassassin()) \
        )

    def test_consul(self):
        self.assertTrue( \
            self.__test_version(ver.check_consul()) \
        )

    def test_mimedefang(self):
        self.assertTrue( \
            self.__test_version(ver.check_mimedefang()) \
        )

    def test_roundcube(self):
        self.assertTrue( \
            self.__test_version(ver.check_roundcube()) \
        )

    def test_vagrant(self):
        self.assertTrue( \
            self.__test_version(ver.check_vagrant()) \
        )

    def __test_version(self, input_values=None):

        if (input_values):
            for value in input_values:
                input_parts = value.split('.')
                if (len(input_parts) <= 1 or len(input_parts) >= 5):
                    return(False)

                for input_part in input_parts:
                    input_num = 0
                    try:
                        input_num = int(input_part)
                    except TypeError:
                        input_num = -1
                    except ValueError:
                        if (len(input_part) < 5):
                            # If it's shorter than 4, it's probably
                            # something like 9.9.1-P3 or 1.3.4b
                            if (re.match('^[A-Za-z0-9_-]*$', input_part)):
                                sys.stdout.write(
                                    ("\n\t"
                                        "Version (%s from %s) seems to "
                                        "contain short chars as extended "
                                        "version? " %
                                        (input_part, value))
                                )
                                sys.stdout.flush()
                                input_num = 0
                            else:
                                input_num = -1
                        elif (input_part.find('-ESV-') > -1):
                            # BIND extended support versions
                            sys.stdout.write(
                                ("\n\t"
                                    "Version (%s from %s) seems to be "
                                    "BIND ESV? " %
                                    (input_part, value))
                            )
                            sys.stdout.flush()
                            input_num = 0
                        else:
                            input_num = -2
                    self.assertGreater(
                        input_num, -1,
                        ("Piece (%s) of version number (%s) didn't "
                         "transfer to int?" % (input_part, value))
                    )
                    self.assertLess(
                        input_num,
                        999,
                        ("Piece (%s) of version number (%s) is higher "
                         "than 999" % (input_part, value))
                    )

            return(True)

        return(False)


def set_include_path():
    include_path = os.path.abspath("../")
    sys.path.append(include_path)


if __name__ == "__main__":
    set_include_path()
    from software_versions import versions as ver

    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVersionFunctions)
    unittest.TextTestRunner(verbosity=3).run(suite)
