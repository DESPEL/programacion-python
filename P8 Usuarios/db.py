import json

with open("data.json", "a") as _:
    pass

data = {}

with open("data.json", "r") as f:
    try:
        data = json.load(f)
    except json.JSONDecodeError:
        data["users"] = []

if not data:
    data["users"] = []


def save_data():
    with open("data.json", "w") as f:
        json.dump(data, f)


def add_user(user_dict):
    data["users"].append(user_dict)
    save_data()
