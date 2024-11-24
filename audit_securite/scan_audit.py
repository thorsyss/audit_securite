from modules.network_scanner import scan_network
from modules.vulnerability_checker import check_vulnerability
from modules.report_generator import generate_report

def run_audit(target):
    # Scanner le réseau
    scan_results = scan_network(target)
    
    # Vérifier les vulnérabilités pour chaque service
    for host in scan_results:
        for service in host["services"]:
            check_vulnerability(service["name"], service["version"])
    
    # Générer le rapport
    generate_report(scan_results)

if __name__ == "__main__":
    target_ip = input("Entrez l'adresse IP ou le réseau à scanner (ex: 192.168.1.0/24) : ")
    run_audit(target_ip)
