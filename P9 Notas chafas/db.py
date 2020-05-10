import json

with open("data.json", "a") as _:
    pass

data = {}

with open("data.json", "r") as f:
    try:
        data = json.load(f)
    except json.JSONDecodeError:
        data["note"] = []

if not data:
    data["note"] = []


def save_data():
    print("Saving data")
    print(data)
    with open("data.json", "w") as f:
        json.dump(data, f)


def add_folder(user_dict):
    data["note"].append(user_dict)
    save_data()
