import os
import requests

# définition de l'adresse de l'API
api_address = '18.201.225.236'
# port de l'API
api_port = 8000

# Informations d'authentification pour Alice
alice_auth = ('alice', 'wonderland')

# Versions à tester
versions = ['v1', 'v2']

# Fonction pour tester l'autorisation pour Alice sur chaque version
def test_authorization():
    for version in versions:
        url = f'http://{api_address}:{api_port}/{version}/sentiment'
        response = requests.get(url, auth=alice_auth)
        if response.status_code == 200:
            print(f"Accès autorisé pour Alice à la version {version}")
        else:
            print(f"Accès refusé pour Alice à la version {version}, Code de statut: {response.status_code}")

# Appel de la fonction pour tester l'autorisation
test_authorization()

# Informations d'authentification pour Bob
bob_auth = ('bob', 'builder')

# Fonction pour tester l'autorisation pour Bob sur chaque version
def test_authorization2():
    for version in versions:
        url = f'http://{api_address}:{api_port}/{version}/sentiment'
        response = requests.get(url, auth=bob_auth)
        if response.status_code == 200:
            print(f"Accès autorisé pour bob à la version {version}")
        else:
            print(f"Accès refusé pour bob à la version {version}, Code de statut: {response.status_code}")

# Appel de la fonction pour tester l'autorisation
test_authorization2()
