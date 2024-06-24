#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


#To loop through a set of code a specified number of times, we can use the range() function,
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

for x in range(2, 30, 3):
  print(x)

#The else block will NOT be executed if the loop is stopped by a break statement

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")