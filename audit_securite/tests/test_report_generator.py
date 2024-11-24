import unittest
from modules.report_generator import generate_report

class TestReportGenerator(unittest.TestCase):

    def test_generate_report(self):
        # Simule des données de scan
        scan_results = [
            {"ip": "192.168.1.1", "status": "up", "services": [{"port": 80, "name": "http"}]}
        ]
        generate_report(scan_results, "test_report.html")
        
        # Vérifie que le fichier existe
        with open("test_report.html", "r") as f:
            content = f.read()
            self.assertIn("<html>", content)
            self.assertIn("Rapport d'Audit de Sécurité", content)

if __name__ == "__main__":
    unittest.main()
