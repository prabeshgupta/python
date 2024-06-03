#JSON stands for Javascript Object Notation. It is used for storing and exchanging data.

import json

#Convert from JSON to Python: We use json.loads() method to parse JSON string into python dictionary

# some JSON string:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


#Convert from Python to JSON: json.dumps() method

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=3, sort_keys=True)) #Add whitespace in the begining 
