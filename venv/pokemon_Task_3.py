import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def calculate_average_weight(pokemon_list):
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list)
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_data_list = []

for name in pokemon_names:
    data = fetch_pokemon_data(name)
    if data:
        pokemon_data_list.append(data)
        abilities = [ability['ability']['name'] for ability in data['abilities']]
        print(f"Name: {data['name']}")
        print("Abilities:", abilities)
    else:
        print(f"Failed to fetch data for {name}")

if pokemon_data_list:
    avg_weight = calculate_average_weight(pokemon_data_list)
    print(f"\nAverage weight of {', '.join(pokemon_names)}: {avg_weight}")