# poke_scraper.py

import requests

def scrape_pokemon_data():
    url = "https://pokeapi.co/api/v2/pokemon/ditto"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  # Wandle die Antwort in ein JSON-Format um
        print(f"Name: {data['name']}")
        print(f"ID: {data['id']}")
    else:
        print("Fehler beim Abrufen der Daten!")

scrape_pokemon_data()