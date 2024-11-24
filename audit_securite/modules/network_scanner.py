import nmap

def scan_network(target):
    # Crée un objet scanner Nmap
    scanner = nmap.PortScanner()

    print(f"Scanning {target}...")
    # Scanner les ports de 1 à 1024
    scanner.scan(hosts=target, arguments='-p 1-1024')

    # Afficher les résultats
    for host in scanner.all_hosts():
        print(f"\nHost: {host}")
        print(f"Status: {scanner[host].state()}")
        
        # Afficher les ports ouverts et les services associés
        for proto in scanner[host].all_protocols():
            print(f"Protocol: {proto}")
            lport = scanner[host][proto].keys()
            for port in lport:
                print(f"Port: {port}\tService: {scanner[host][proto][port]['name']}")

if __name__ == "__main__":
    target_ip = input("Entrez l'adresse IP ou le réseau à scanner (ex: 192.168.1.0/24) : ")
    scan_network(target_ip)
