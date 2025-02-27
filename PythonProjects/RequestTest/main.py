import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'cYour_token'
HEADER = {'Content-Type' : 'application/json','trainer_token' :TOKEN}

body_create = {
    "name": "ПИТОН",
    "photo_id": -1
}

body_name = {
    "pokemon_id":"246411",
    "name": "New Name",
    "photo_id": 3
}

body_add = {
    "pokemon_id": "246407"
}


'''response_create =  requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)'''


'''response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)'''


'''response_add =  requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(response_add.text)'''