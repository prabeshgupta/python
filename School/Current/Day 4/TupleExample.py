#Create a tuple with names "Ram", "Shyam" and "Hari" and add "Rita"

names = ("Ram", "Shyam", "Hari")
names_list  = list(names)
names_list.append("Rita")
names = tuple(names_list)
print(names)