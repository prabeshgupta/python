#Scope defines where a variable is accessible and where it is not.

x = 300

def myfunc():
  global x
  x = 200
  print(x)

myfunc()



"""
The nonlocal keyword is used to declare that a variable inside a nested function is not local to it, nor global. Instead, it refers to a variable in the nearest enclosing scope.
"""

def outer_function():
    x = 10
    
    def inner_function():
        nonlocal x #it refers to the x defined in outer_function(). So, when inner_function() modifies x, it modifies the x in outer_function() as well.
        x = 20
        print("Inner function:", x)
    
    inner_function()
    print("Outer function:", x)

outer_function()
