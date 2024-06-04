#The key function for working with files in Python is the open() function. The open() function takes two parameters; filename, and mode.

"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

"""

import os

#Create a new file
f = open("C:\\Users\gamerzchoices\Documents\CODING\python\Home\Day 8\File.txt", "x")


#Write/Update a file
f= open("C:\\Users\gamerzchoices\Documents\CODING\python\Home\Day 8\File.txt","a")
f.write("Hello World")
f.close()

#Read a file
f= open("C:\\Users\gamerzchoices\Documents\CODING\python\Home\Day 8\File.txt","r")
print(f.read())
f.close()

#Delete a file
os.remove("C:\\Users\gamerzchoices\Documents\CODING\python\Home\Day 8\File.txt")

#Delete a empty folder
os.rmdir("C:\\Users\gamerzchoices\Documents\CODING\python\Home\Day 8\\rm")