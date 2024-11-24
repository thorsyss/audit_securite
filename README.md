# audit_securite
Script d'automatisation pour les audits de sécurité réseau.

# Projet d'Automatisation d'Audits de Sécurité

## Description

Ce projet permet d'automatiser les audits de sécurité d'un réseau en utilisant des outils tels que **Nmap** pour scanner les ports et services, et des vérifications de vulnérabilités pour chaque service détecté. Un rapport détaillé est généré à la fin de l'audit pour permettre une analyse complète des risques.

L'objectif est de faciliter les tests de pénétration, de découvrir des vulnérabilités sur des réseaux ou des systèmes, et de produire des rapports exploitables.

## Fonctionnalités

1. **Scan de réseau** :
   - Scanne un réseau ou une machine cible pour détecter les ports ouverts et les services associés.
   
2. **Vérification des vulnérabilités** :
   - Vérifie les vulnérabilités connues associées aux services détectés (par exemple, version de service vulnérable à des attaques).

3. **Génération de rapport** :
   - Génère un rapport HTML détaillant les hôtes analysés, leurs services et les vulnérabilités associées.

## Structure du Projet

Voici la structure du projet et son explication :

audit_securite/
├── README.md
├── requirements.txt
├── scan_audit.py
├── modules/
│   ├── network_scanner.py
│   ├── vulnerability_checker.py
│   └── report_generator.py
├── reports/
│   ├── report_YYYYMMDD.html
│   └── report_YYYYMMDD.pdf
├── tests/
│   ├── test_network_scanner.py
│   ├── test_vulnerability_checker.py
│   └── test_report_generator.py



## Installation

### Prérequis

- **Python 3.x** : Si vous n'avez pas Python installé, vous pouvez le télécharger sur [python.org](https://www.python.org/downloads/).
- **Nmap** : Utilisé pour scanner les réseaux et les ports.
  
  Téléchargez et installez **Nmap** à partir de [nmap.org](https://nmap.org/download.html). Après installation, assurez-vous que la commande `nmap` est disponible dans votre terminal.

### Installation des dépendances

1. Clonez ce projet :
   ```bash
   git clone https://github.com/thorsyss/audit_securite.git
   cd audit_securite




