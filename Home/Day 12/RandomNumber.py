#Random means something that can not be predicted logically.

# Random numbers generated through a generation algorithm are called pseudo random.

from numpy import random

x=random.randint(100, size=5) #Array
print(x)


x = random.rand() #Float between 0 and 1
print(x)