import numpy as np

#Array with row 5 and column 1 containing 0
print(np.zeros((5,1)))

#Array with rows 5 and columns 3 containing 1
print(np.ones((5,3)))

#Array with unit matrix
print(np.eye(3))

#Initized Array
A = np.array([[1,3,4], [5,6,7]])
B = np.array([[3,4,6], [3,7,4]])
C = np.zeros((2,3))
C = A + B
print(C)

# Square Root
print(np.sqrt(A))

#Exponential (e^x = 2.718^x)
D = np.array([0,1,3,4])
E = np.exp(D)
print(E)

#Add
print(np.sum(A))

#Mean
print(np.mean(A))

#Min
print(np.min(A))
