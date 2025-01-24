#Dictionary from two list

keys = ["name", "age", "address"]
values = ["Prabesh",22, "Nepal"]

# myDict = dict(zip(keys, values))
# print(myDict)


info={}
for i in range(len(keys)):
    info[keys[i]] = values[i]
print(info)