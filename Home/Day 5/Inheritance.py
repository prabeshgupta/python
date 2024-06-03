#Inheritance is the passing of parent properties and method to its children.
#Parent class(Base class) is the class which is being inherited and child class(derived class) is the class that inherits the another class.

#To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class.

class ParentClass:
    x=10

class ChildClass(ParentClass):
   pass

cC = ChildClass()
print(cC.x)

#super() function makes the child class inherit all the methods and properties from its parent

class ParentClass:
    def __init__(self, val1):
        self.val1 =val1

    def display(self):
        return self.val1

class ChildClass(ParentClass):
   def __init__(self, val1, val2):
       super().__init__(val1)
       self.val2 =  val2

cC = ChildClass(10,100)
print(cC.val1,cC.val2)
