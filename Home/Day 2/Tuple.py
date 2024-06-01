#A tuple is a collection which is unchangeable written with round brackets.

#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

thistuple = ("apple",)
print(type(thistuple))

#Tuple are unchangeable so we need to change to list.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

green, yellow, *red = fruits

print(green)
print(yellow)
print(red)
