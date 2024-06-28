#Function is a block of code that only runs when it is called.

#Parameters are the variables present inside the parenthesis of the function defination.

#Arguments are the values that are sent to the function when it is called.

#Arbitary arguments (*args): It receives the tuple of arguments.
def display(*data):
    print(f"My name is {data[0]}")
display("Prabesh","Gupta",22)


#Keyword arguments(kwargs)

def name(name1, name3, name2):
    print(f"I love {name2}")
name(name1="Prabesh", name2="Upahar", name3="Sanu")

#Arbitary keyword arguments(**kwargs): It receives the dictionary of arguments.

def game(**data):
    print("I hate "+ data["three"])

game(one = "football", two="cricket", three="kabadi")


#Default value in parameter
def country(visit = "Nepal"):
    print(visit)

country("USA")
country()


#Postional only arguments(, /)
def my_function(x, /):
  print(x)

my_function(3)


#keyword only arguments(*,)
def message(*, event):
    print(event)

message(event="New Year 2081")


#combination
def my_function(a, /, *, b):
  print(a + b)

my_function(6, b = 7)


#Recursion

def factorial(num):
    if num>0:
        result = num * factorial(num-1)
    else:
        return 1
    return result
print(factorial(4))
      
