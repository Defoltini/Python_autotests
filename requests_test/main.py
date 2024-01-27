import requests

#Создание покемона#

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json', 
'trainer_token': '1dcbeea233df76bc8da6dc7c4a517115'}

body = {
    "name": "generate",
    "photo": "generate"
}
response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print (f'Результат выполнения запроса: {response.text}') 

#Поймать покемона в покебол#

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json', 
'trainer_token': '1dcbeea233df76bc8da6dc7c4a517115'}

body = {
    "pokemon_id": "28720"
}
response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER, timeout=5)
print (f'Результат выполнения запроса: {response.text}') 

#Смена имени покемона#

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json', 
'trainer_token': '1dcbeea233df76bc8da6dc7c4a517115'}

body = {
    "pokemon_id": "28708",
    "name": "karl",
}
response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print (f'Новые данные покемона: {response.text}') 