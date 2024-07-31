import requests

def fetch_pokemon_data(pokemon_name):
    total_weight = 0

    for pokemon_name in pokemon_names:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
        pokemon_data = response.json()
        
        print(f"Name of Pokemon: {pokemon_data["name"]}")
        print(f"Abilities: {', '.join(ability['ability']['name'] for ability in pokemon_data['abilities'])}")
        print(f"Weight of the Pokemon: {pokemon_data["weight"]}")

        total_weight += pokemon_data['weight']
    
    print("this is the avg weight", total_weight / len(pokemon_names))
   
pokemon_names = ["pikachu", "charmander", "bulbasaur"]

fetch_pokemon_data(pokemon_names)