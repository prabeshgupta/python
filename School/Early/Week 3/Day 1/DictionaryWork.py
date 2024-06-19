#Key Value Dictionary

info={
    "name":"Prabesh",
    "age": 22,
    "class": "BCA"
}

[print(key, val) for key,val in info.items() if key == "name" or key =="class"]

print()

for key in info.keys():
    print(key)

for val in info.values():
    print(val)