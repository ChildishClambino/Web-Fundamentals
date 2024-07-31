import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    heaviest_planet = None
    max_mass = 0
    
    for planet in planets:
  
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue']
            orbit_period = planet['sideralOrbit']
            print(f"\n\nPlanet: {name}\nMass: {mass}\nOrbit Period: {orbit_period} days")

            if mass > max_mass:
                max_mass = mass
                heaviest_planet = name
    
    if heaviest_planet:
        print(f"The heaviest planet is {name} with a mass of {mass} kg.")

fetch_planet_data()