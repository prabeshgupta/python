A = [[1,3,5],[2,4,6]]
B= [[7,9,11], [8,10,12]]
C = [[0,0,0],[0,0,0]]

rows = len(A)
columns = len(A[1])

print(rows, columns)

for i in range(rows):
    for j in range(columns):
        C [i][j]= A[i][j] + B[i][j]

print(C)