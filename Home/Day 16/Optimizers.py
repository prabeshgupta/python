#Optimizers are a set of procedures defined in SciPy that either find the minimum value of a function, or the root of an equation.

#Calculate non-linear equation
"""
This function takes two required arguments:

fun - a function representing an equation.

x0 - an initial guess for the root.
"""

from scipy.optimize import root
from math import cos

def eqn(x):
  return x + cos(x)

myroot = root(eqn, 0)

print(myroot.x)

"""
A function, represents a curve, curves have high points and low points.

High points are called maxima.

Low points are called minima.

The highest point in the whole curve is called global maxima, whereas the rest of them are called local maxima.

The lowest point in whole curve is called global minima, whereas the rest of them are called local minima.
"""