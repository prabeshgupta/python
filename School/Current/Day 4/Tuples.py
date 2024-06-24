#Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable.
#Tuples are written with round brackets.

games = ("football", "cricket", "volleyball", "football")
print(games)

#Print the last item
print(games[-1])

#One item tuple
game  =  ("football",)
print(game)

#Tuples are unchangeable or immutable, meaning that you cannot change, add, or remove items once the tuple is created.

sports =  ("hockey","badminton", "carrom")
sports_list  =  list(sports)
sports_list[1] =  "table tennis"
sports  = tuple(sports_list)
print(sports)


#When we create a tuple, we assign values to it. This is called "packing" a tuple. But, we are also allowed to extract the values back into variables. This is called "unpacking".

(first, second, third) = sports
print(first)

#The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

(one, *two) = games
print(two)