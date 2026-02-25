import json

name = {"first": "John", "last": "Doe","present":True}

js_obj = json.dumps(name)
print(js_obj)

with open("try.json", "w") as f:
    data = json.dump(name, f,indent=4)


json_data = '{"name": "John", "age": 25}' 
python_obj = json.loads(json_data)
print(python_obj["name"])