#Make a list
myList  = list(("apple", "banana", 44))
print(myList)

#List to get the first item in reverse order
fruit_list = ["apple", "banana", "cherry"]
print(fruit_list[-1])

#List change items
fruit_list[1:3] = ["blueberry","mango"]
print(fruit_list)

#Insert at specified index
fruit_list.insert(2, "watermelon")
print(fruit_list)

#Append a item in end
fruit_list.append("orange")
print(fruit_list)

#Merge two lists into one
fruit_list = ["apple", "banana", "cherry"]
more_list = ["grapes", "pineapple", "papaya"]
fruit_list.extend(more_list)

fruit_tuple = ("dragon fruit", "kiwi", "strawberry")
fruit_list.extend(fruit_tuple)
print(fruit_list)

#Remove the item from list
fruit_list.remove("dragon fruit")

#Remove item of specified index
fruit_list.pop(4)
del fruit_list[1]
print(fruit_list)

#Loop list items
for i in range(len(fruit_list)):
    print(fruit_list[i])

#Sort list in ascending order
fruit_list.sort()
print(fruit_list)

#Sort list in descending order
fruit_list.sort(reverse=True)
print(fruit_list)

#Reverse a list
fruit_list.reverse()
print(fruit_list)

#Copy a list
fruit_basket =  fruit_list.copy()
print(fruit_basket)