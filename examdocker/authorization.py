import os
import requests

# définition de l'adresse de l'API
api_address = '3.254.195.81'
# port de l'API
api_port = 8000

# requête
r = requests.get(
    url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland'
    }
)




output = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="alice"
| password="wonderland"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''


# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output)




# requête
r = requests.get(
    url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
    params= {
        'username': 'bob',
        'password': 'builder'
    }
)

output = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="bob"
| password="builder"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == '1':
    with open('api_test.log', 'a') as file:
        file.write(output)

# requête
r = requests.get(
    url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
    params= {
        'username': 'clementine',
        'password': 'mandarine'
    }
)

output = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="clementine"
| password="mandarine"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == '1':
    with open('api_test.log', 'a') as file:
        file.write(output)




########################content########################


# Définition des informations d'authentification pour Alice
utilisateurs = [{'username': 'alice', 'password': 'wonderland'}]

# Phrases à analyser
phrases = [
    "life is beautiful",
    "that sucks"
]

# Fonction pour effectuer les requêtes de test pour chaque utilisateur et chaque phrase
def effectuer_tests():
    for utilisateur in utilisateurs:
        for phrase in phrases:
            for version in ['v1', 'v2']:
                url = f'http://{api_address}:{api_port}/{version}/sentiment'
                auth = (utilisateur['username'], utilisateur['password'])
                params = {'sentence': phrase}
                response = requests.get(url, auth=auth, params=params)
                if response.status_code == 200:
                    score = response.json().get('score')
                    if score is not None:
                        print(f"Utilisateur: {utilisateur['username']}, Version: {version}, Phrase: '{phrase}', Score: {score}")
                    else:
                        print(f"Impossible de récupérer le score pour la phrase '{phrase}'")
                else:
                    print(f"Échec de la requête pour la phrase '{phrase}' avec l'utilisateur {utilisateur['username']} et la version {version}, Code de statut: {response.status_code}")

# Appel de la fonction pour effectuer les tests
effectuer_tests()






# Informations d'authentification
utilisateurs = [
    {'username': 'alice', 'password': 'wonderland'},
    {'username': 'bob', 'password': 'builder'}
]

# Fonction pour tester l'authentification pour chaque utilisateur
def test_authentication():
    for utilisateur in utilisateurs:
        url = f'http://{api_address}:{api_port}/permissions'
        response = requests.get(url, auth=(utilisateur['username'], utilisateur['password']))
        if response.status_code == 200:
            print(f"Authentification réussie pour l'utilisateur {utilisateur['username']}")
        else:
            print(f"Échec de l'authentification pour l'utilisateur {utilisateur['username']}, Code de statut: {response.status_code}")

# Appel de la fonction pour tester l'authentification
test_authentication()



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



# Informations d'authentification pour Alice
alice_auth = ('bob', 'builder')

# Phrases à tester
phrases = [
    "life is beautiful",
    "that sucks"
]

# Fonction pour tester le contenu pour Alice avec chaque phrase
def test_content():
    for phrase in phrases:
        for version in ['v1']:
            url = f'http://{api_address}:{api_port}/{version}/sentiment'
            response = requests.get(url, auth=alice_auth, params={'sentence': phrase})
            if response.status_code == 200:
                score = response.json().get('score')
                print(f"Phrase: '{phrase}', Version: {version}, Score: {score}")
            else:
                print(f"Échec de la récupération du score pour la phrase '{phrase}' et la version {version}, Code de statut: {response.status_code}")

# Appel de la fonction pour tester le contenu
test_content()



# requête
r = requests.get(
    url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland'
    }
)




output = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="alice"
| password="wonderland"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''


# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output)




##################
# requête
r = requests.get(
    url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
         'sentence': ['life is beautiful']
    }
)


output = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="alice"
| password="wonderland"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# Affichage du résultat de la requête pour tester le contenu
print("\nRésultat de la requête pour tester le contenu:")
print("Code de statut:",r.status_code)
print("Contenu de la réponse:", r.text)


#################
# requête
r = requests.get(
    url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
         'sentence': ['that suck']
    }
)


output = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="alice"
| password="wonderland"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# Affichage du résultat de la requête pour tester le contenu
print("\nRésultat de la requête pour tester le contenu:")
print("Code de statut:",r.status_code)
print("Contenu de la réponse:", r.text)
# impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output)# requête

#################
# requête
r = requests.get(
    url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
         'sentence': ['life is beautiful']
    }
)


output = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="alice"
| password="wonderland"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# Affichage du résultat de la requête pour tester le contenu
print("\nRésultat de la requête pour tester le contenu:")
print("Code de statut:",r.status_code)
print("Contenu de la réponse:", r.text)

#################
# requête
r = requests.get(
    url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
         'sentence': ['life sucks']
    }
)


output = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="alice"
| password="wonderland"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# Affichage du résultat de la requête pour tester le contenu
print("\nRésultat de la requête pour tester le contenu:")
print("Code de statut:",r.status_code)
print("Contenu de la réponse:", r.text)


#################
# requête
r = requests.get(
    url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'bob',
        'password': 'builder',
         'sentence': ['life is beautiful']
    }
)


output = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="alice"
| password="wonderland"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# Affichage du résultat de la requête pour tester le contenu
print("\nRésultat de la requête pour tester le contenu:")
print("Code de statut:",r.status_code)
print("Contenu de la réponse:", r.text)


#################
# requête
r = requests.get(
    url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'bob',
        'password': 'builder',
         'sentence': ['that sucks']
    }
)


output = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="alice"
| password="wonderland"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# Affichage du résultat de la requête pour tester le contenu
print("\nRésultat de la requête pour tester le contenu:")
print("Code de statut:",r.status_code)
print("Contenu de la réponse:", r.text)
