#Casting
name = str("Prabesh Gupta")
age = int(22)

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types.
print(name, age)


#Unpacking
games = ['MLBB', 'COC']
g1, g2 = games

print(g1, g2)


#Local variable and global variable
name = "Upahar"
def display():
    #Local
    name = "Shristi"
    print(name)
    #Global
    global age
    age = 22
display()
print(name,age)
