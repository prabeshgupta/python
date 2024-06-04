#F-string allows you to format selected parts of a string.

#Placeholder with legal formating type
txt = f"The price is {49:.2f} dollars"
print(txt)

#Placeholder with Function
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)