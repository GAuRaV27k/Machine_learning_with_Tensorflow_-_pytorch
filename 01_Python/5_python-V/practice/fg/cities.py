import json

with open("city.json", "r") as f:
    data = json.load(f)
    for city in data["cities"]:
        print(f"City: {city['name']}, Country: {city['country']}, Population: {city['population']}")