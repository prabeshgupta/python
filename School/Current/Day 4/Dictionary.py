#Dictionaries are used to store data values in key:value pairs.

info = dict(name = "John", age = 36, country = "Kavre")
print(info)

#Alternate way to get value of key
print(info.get("name"))

print(info.keys())
print(info.values())
print(info.items()) #The items() method will return each item in a dictionary, as tuples in a list.

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"year": 2020,"milage":100})
print(car)

#The pop() method removes the item with the specified key name
car.pop("milage")

#popitem() removes the last item


#Nested dictionary
