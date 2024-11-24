from jinja2 import Template

def generate_report(scan_results, filename="audit_report.html"):
    # Template HTML basique
    report_template = """
    <html>
        <head><title>Rapport d'Audit de Sécurité</title></head>
        <body>
            <h1>Rapport d'Audit de Sécurité</h1>
            {% for host in scan_results %}
            <h2>Hôte: {{ host.ip }}</h2>
            <p>Status: {{ host.status }}</p>
            <table border="1">
                <tr><th>Port</th><th>Service</th></tr>
                {% for service in host.services %}
                <tr>
                    <td>{{ service.port }}</td>
                    <td>{{ service.name }}</td>
                </tr>
                {% endfor %}
            </table>
            {% endfor %}
        </body>
    </html>
    """
    
    # Création du template Jinja2
    template = Template(report_template)
    report_html = template.render(scan_results=scan_results)
    
    # Sauvegarde du rapport HTML
    with open(filename, "w") as f:
        f.write(report_html)
    print(f"Rapport généré dans {filename}")

if __name__ == "__main__":
    # Exemple de résultats de scan simulés
    scan_results = [
        {
            "ip": "192.168.1.1",
            "status": "up",
            "services": [{"port": 80, "name": "http"}, {"port": 22, "name": "ssh"}]
        },
        {
            "ip": "192.168.1.2",
            "status": "down",
            "services": []
        }
    ]
    
    generate_report(scan_results)
