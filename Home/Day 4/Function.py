#A function is a block of code which only runs when it is called.

"""
From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.
"""

#Arbitary Arguments: If the number of arguments is unknown, add a * before the parameter name. The function will receive a tuple of arguments.

def display(*boss):
    print(f"Hello, {boss[0]}")
display("Prabesh","Gupta")

#Arbitary keyword arguments:If the number of keyword arguments is unknown, add a double ** before the parameter name. The function will receive a dictionary of arguments

def go(**now):
    print("Tour "+now["nepal"])
go(nepal = "Kathmandu", india="New Delhi")


#To let a function return a value, use the return statement


#Recursion means that a function calls itself
def recursionAdd(num):
    if num>0:
        add = num + recursionAdd(num -1)
    else:
        return 0
    return add

print(recursionAdd(10))

def recursionMul(num):
    if num>0:
        mul = num * recursionMul(num -1)
    else:
        return 1
    return mul
print(recursionMul(5))