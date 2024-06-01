#You can return a range of characters by using the slice syntax.

city = "Kathmandu City"
sliced = city[3:10] # end index 10 is excluded
print(sliced)

#Negative Indexing: Use negative indexes to start the slice from the end of the string
negslice = city[-13:-1]
print(negslice)

#Reverse
rev = city[::-1]
print(rev)

#Whitespace remove
brand = "Apple Ipad "
print(brand.strip())

#Split: Splits the string at the specified separator, and returns a list

money= "USD,EUR,GBP"
print(money.split(','))


#To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables.
age = 22
print(f"I am {age} years old.")

#A placeholder can contain variables, operations, functions, and modifiers to format the value. The placeholder is defined using curly brackets: {}

#A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals.
price = 22
print(f"Price is Rs {price:.2f}")


#If the value is not found, the find() method returns -1, but the index() method will raise an exception:
txt = "Hello, welcome to my world."

print(txt.find("q"))
#print(txt.index("q"))


#The format() method formats the specified value(s) and insert them inside the string's placeholder.

print("This is awesome {year}".format(year=2024))
print("Time is {0}:{1}".format(12,17))
print("I am in BCA {} year".format(3))


#join is used to combine the tuple values in single string
book  = ('Nepali', 'English')
print(''.join(book))