"""
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""

try:
  x=10
  print(x)
except NameError:
  print("Variable x is not defined")
else:
  print("All went right")
finally:
  print("I don't know what to do.")


#Raise an exception: Throw an exception if a condition occurs.

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
