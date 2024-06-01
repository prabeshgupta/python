#Dictionary: One of the 4 data type to store collection of data in key: value pairs.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict.keys():
  print(x)

for y in thisdict.values():
  print(y)

for x, y in thisdict.items():
  print(x, y)


#Nested Dictionary

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

#Alternative way
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
}

print(myfamily["child2"]["name"])


