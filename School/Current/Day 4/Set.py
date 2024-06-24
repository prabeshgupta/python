#Sets are used to store multiple items in a single variable enclosed in curly brackets.

#True and 1 is considered the same value. False and 0 are considered the same value in sets, and are treated as duplicates
mySet = {0,"apple", "banana", "cherry", True, 1, 2, False}

#Add item
mySet.add("Solo Leveling")
print(mySet)


#To add items from another set into the current set, use the update() method. The update() changes the original set, and does not return a new set.



new_animes = {"Solo Leveling","Spy X Family"}
old_animes = {"Naruto","One Piece"}
new_animes.update(old_animes)
print(new_animes)

#If the item to remove does not exist, remove() will raise an error but discard() don't raise an error.
new_animes.discard("Spy X Famil")
print(new_animes)


# The union() and update() methods joins all items from both sets. Returns a new set

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2) # set1 | set2
print(set3)

# The intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"a", "b", "c"}
set2 = {"b", "d", "e"}

set3 = set1.intersection(set2) #set1 & set2
print(set3)

#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2) #set1 - set2
print(set3)


# The symmetric_difference() method will keep only the elements that are NOT present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2) #set1 ^ set2

print(set3)

set4 = set1.copy()
print(set4)