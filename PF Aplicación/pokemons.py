import json
import requests


def get_pokemon_interval(start, end):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit={end-start}&offset={start}')
    return json.loads(response.text)

if __name__ == "__main__":
    print(get_pokemon_interval(0, 50))