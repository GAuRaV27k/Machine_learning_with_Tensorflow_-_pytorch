# words = ["apple", "banana", "kiwi", "cherry", "mango"]


words = ["apple", "banana", "kiwi", "cherry", "mango"]
dct ={}
print("Now we are creating the map")
for item in words:
    key = input(f"Enter the value of {item} :")
    new = {item : key}
    dct.update(new)

print(dct.items())

