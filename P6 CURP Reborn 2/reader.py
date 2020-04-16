import json

abreviaciones = {}

with open("claves_estados.json", "r", encoding="utf-8") as f:
    abreviaciones = json.load(f)
