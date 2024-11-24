import unittest
from modules.network_scanner import scan_network

class TestNetworkScanner(unittest.TestCase):

    def test_scan_single_host(self):
        # Simule un scan sur une IP de test
        result = scan_network('127.0.0.1')  # une IP locale loopback
        self.assertIn('127.0.0.1', result)
        self.assertIn('80', result['127.0.0.1'])  # Vérifie que le port 80 est ouvert
        
    def test_scan_multiple_hosts(self):
        result = scan_network('192.168.1.0/24')  # Un sous-réseau local à tester
        self.assertTrue(len(result) > 0, "Le scan devrait trouver des hôtes")
        
    def test_no_ports_open(self):
        result = scan_network('192.168.1.10')  # IP d'un hôte sans services
        self.assertEqual(result['192.168.1.10']['state'], 'down')

if __name__ == "__main__":
    unittest.main()
