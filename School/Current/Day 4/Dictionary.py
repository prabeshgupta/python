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


###############################################################

#Empty dictionary 
#a = {}
#b = dict()
print(type({}))


#Key should be unique
data = {"Ram":22,"Shyam":48,"Ram":24}
print(len(data))
print(data)

#Behind the scene when we change the value of the "Ram" then it adds to the end of the dictionary so it will update to the new value


#Nested Dictionary
info = {
    "person1":{
        "name":"Prabesh",
        "age": 22
    },
    "person2":{
        "name":"Upahar",
        "age":21
    }
}
info["person1"]["age"] =23
print(info["person1"]["age"])


#Zip

c = [1,3,4]
d = [3,4,6]
for e,f in zip(c,d):
    print(e,f)