import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    
    if response.status_code == 200:
        planets = [planet for planet in response.json()['bodies'] if planet['isPlanet']]
        return planets
    else:
        print("Failed to fetch data.")
        return []

def find_heaviest_planet(planets):
    heaviest_planet = max(planets, key=lambda planet: planet.get('mass', {}).get('massValue', 0))
    name = heaviest_planet['englishName']
    mass = heaviest_planet.get('mass', {}).get('massValue', 'Unknown')
    return name, mass

planets = fetch_planet_data()

for planet in planets:
    name = planet['englishName']
    mass = planet.get('mass', {}).get('massValue', 'Unknown')
    orbit_period = planet.get('sideralOrbit', 'Unknown')
    print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

name, mass = find_heaviest_planet(planets)
print(f"\nThe heaviest planet is {name} with a mass of {mass} kg.")
