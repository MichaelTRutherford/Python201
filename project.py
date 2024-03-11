# 1. Ask for user input -> ditto
# 2. Create a dynamic URL based on step 1
# 3. Fetch the data from the url in step 2
# 4. Convert JSON to a dictionary
# 5. Print out pokemon data

import requests

while True:
    species = input("Which pokeman do you want to find? ")
    species = species.lower()

    url = f"https://pokeapi.co/api/v2/pokemon/{species}"

    req = requests.get(url)
    if req.status_code == 200:
        pokemon = req.json()
        print(f"Name is\t\t{pokemon['name']}")
        species = pokemon['species']
        print(f"Species is\t{species['name']}")

        print("Abilities:")
        for ability in pokemon['abilities']:
            print(ability['ability']['name'])
    else:
        print("Pokemon not found")
