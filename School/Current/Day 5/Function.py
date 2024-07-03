#Function is a block of code that only runs when it is called. It is similar to the function of the maths that takes the input, process and returns some output. You can reuse the functions.

#Parameters are the variables present inside the parenthesis of the function defination.

#Arguments are the values that are sent to the function when it is called.

#Identifier is the name of the class, object, variable or functions.

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


#Return keyword is used to reuse the value processed by the function.
def sub(a,b):
    return a-b
    print("Success")

data = sub(10,0)
if data > 9:
    print("Processed successfully")




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
      

#########################################################

#Types of arguments

#Positional arguments -> Order matters. If the order is mismatched then results is unreliable.

def num(a,b):
    print(a+b)
num(2,3)


#Keyword arguments -> Order don't matter. Keyword is specific word that we send to the parameter.

def name(fname, lname, mname):
    print(f"Hello, {fname} {mname} {lname}.")
name(mname="Ashoka", fname="Puran", lname="Somban")