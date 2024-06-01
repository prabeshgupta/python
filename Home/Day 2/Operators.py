#Arithmetic Operator

print(5**8) #Exponent operator
print(8//5) #Floor Divison

#Assignment Operator

print(x := 10)
# x = 10
# print(x)

#Logical operator

if 4<10 and 5>6:
    print(True)

if 4<10 or 5>6:
    print(True)

if not(10<4):
    print(True)


#Identity operator: Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # returns True because both variables are same object

print(x is not y) # returns True because both variables are not same object


#Membership Operators: Test if a sequence is presented in an object.

planets =  ['earth', 'mars']
print('earth' in planets)
print("pluto" not in planets)


#Operator precedence (), **, * /, + -
