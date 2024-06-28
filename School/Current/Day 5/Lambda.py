#A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.

x = lambda a,b : a + b
print(x(5,10))


def num(n):
    return lambda a : a * n

pass_num = num(2) # pass_num now holds the lambda function lambda a: a * 2
print(pass_num(10))