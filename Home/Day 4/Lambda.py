#A lambda function is a small anonymous function.
#lambda arguments : expression

x = lambda a,b: a+b
print(x(10,20))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
