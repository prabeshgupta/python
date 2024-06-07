# Data Distribution is a list of all possible values, and how often each value occurs.

"""
A random distribution is a set of random numbers that follow a certain probability density function.

Probability Density Function: A function that describes a continuous probability. i.e. probability of all values in an array.

The probability lies between 0 and 1, where 0 means that the value will never occur and 1 means that the value will always occur. The sum of all probability numbers should be 1.
"""

from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)