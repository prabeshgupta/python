#Basic for loop
for i in range(10):
    print(i)

#Looping string 
name = "Prabesh Gupta"

for i in name:
    print(i)

for j in range(len(name)):
    print(name[j])

for k in range(0, len(name), 2):
    print(name[k])


#Looping list
games = ["Football", "Cricket", "WWE","Basketball", "Volleyball"]
for i in games:
    print(i)

for j in range(len(games)):
    print(games[j])

for k in range(1, len(games),2):
    print(games[k])


#Looping through tuples

fruits = ("Mango", "Guava", "Apple", "Banana")

for i in fruits:
    print(i)

for j in range(len(fruits)):
    print(fruits[j])

for k in range(0, len(fruits), 3):
    print(fruits[k])


#Looping through set
giants = {"Meta", "Apple", "Microsoft", "Google", "Tesla"}

for i in giants:
    print(i)


#Looping through dictionary

brand = {
    "name": "Rolce Royace",
    "model": "Ghost",
    "price": 10e7
}

for i in brand.keys():
    print(i)

for j in brand.values():
    print(j)

#Tuples in the list. [(a,3),(b,5)] Unpacking the tuple the values in i an j
for i, j in brand.items():
    print(i,j)