#List is represented in []. List is a collection which is changeable (can be added or removed). Allows duplicate members.

#Negative Indexing: Negative indexing means start from the end
#-1 refers to the last item, -2 refers to the second last item etc.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-1])
print(thislist[-4:-1]) #exclude -1 but include -4

market = "Monopolistic"
print(market[-4:-1]) #exclude -1 but include -4


#Insert: To insert a new item, without replacing any of the existing values, we can use the insert() method.

#Append: To add an item to the end of the list, use the append() method.

#Extend: To append elements from another list to the current list or to add multiple new items to list from tuples, sets and dictionaries, use the extend() method.

#Remove: The remove() method removes the specified item.

#Pop: The pop() method removes the specified index.

#Del: The del keyword also removes the specified index or delete the list completely

flower = ['rose', 'lotus', 'jasmine']
del flower[1]
print(flower)

del flower

#Clear: The clear() method empties the list.


#List Comprehension: Shortest list looping syntax.

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] 

#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#newlist = [expression for item in iterable if condition == True] 

#The expression is the current item in the iteration and the outcome.

#The iterable can be any iterable object, like a list, tuple, set etc.

#The condition is like a filter that only accepts the items that valuate to True.

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

"""
extend() method for lists in Python doesn't return a new list; instead, it modifies the original list in place. So when you try to assign the result of list1.extend(list2) to list3, it will be None because that's what extend() returns."""







