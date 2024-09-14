import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    
    if response.status_code == 200:
        planets = response.json()['bodies']
        for planet in planets:
            if planet['isPlanet']:
                name = planet['englishName']
                mass = planet.get('mass', {}).get('massValue', 'Unknown')
                orbit_period = planet.get('sideralOrbit', 'Unknown')
                print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
    else:
        print("Failed to fetch data from API.")

# Call the function to display data
fetch_planet_data()
