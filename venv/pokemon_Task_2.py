#task 2
import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
pokemon_data = fetch_pokemon_data("pikachu")

if pokemon_data:
    name = pokemon_data['name']
    abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
    print(f"Name: {name}")
    print("Abilities:", abilities)
else:
    print("Failed to fetch data.")