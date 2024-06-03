#Class is a blueprint for creating objects.

class MyClass:
    #Property
    x=10

myClass =  MyClass()
print(myClass.x)

"""
All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created.
"""

#The __init__() function is called automatically every time the class is being used to create a new object.

class Anime:
    def __init__(self, top, bottom):
      self.top = top
      self.bottom = bottom

anime = Anime("Naruto", "One piece")
print(anime.top, anime.bottom)


#The __str__() function controls what should be returned when the class object is represented as a string.

class Anime:
    def __init__(self, top, bottom):
      self.top = top
      self.bottom = bottom

    def __str__(self):
       return f"{self.top}"

anime = Anime("Naruto", "One piece")
print(anime)
