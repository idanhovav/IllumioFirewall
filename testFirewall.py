import unittest
from unittest import TestCase
import sys
import firewall as fw

testFileName = "testRules.csv"

class TestFirewall(TestCase):

    @classmethod
    def setUpClass(cls):
        return

    @classmethod
    def tearDownClass(cls):
        return

    def testBasicFunctionality(self):
        firewall = fw.Firewall(testFileName)
        self.assertTrue(firewall.accept_packet("inbound", "tcp", 80, "192.168.1.2"))
        self.assertTrue(not firewall.accept_packet("inbound", "tcp", 81, "192.168.1.2"))
        self.assertTrue(not firewall.accept_packet("inbound", "tcp", 80, "192.168.1.3"))

        self.assertTrue(firewall.accept_packet("outbound", "udp", 13, "192.192.192.192"))
        self.assertTrue(firewall.accept_packet("outbound", "udp", 12, "192.192.192.192"))
        self.assertTrue(not firewall.accept_packet("outbound", "udp", 13, "192.192.192.194"))
        self.assertTrue(not firewall.accept_packet("outbound", "tcp", 13, "192.192.192.192"))

if __name__ == '__main__':
    unittest.main()
