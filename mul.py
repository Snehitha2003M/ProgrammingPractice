r = 3
col = 3

a = [
    [2, 5, 6],
    [1, 8, 4],
    [3, 7, 0]
]

b = [
    [3, 5, 6],
    [4, 6, 8],
    [7, 6, 0]
]

c = [[0 for i in range(col)] for j in range(r)]

print("Matrix A:")
for i in range(r):
    for j in range(col):
        print(a[i][j], end=" ")
    print()

print("Matrix B:")
for i in range(r):
    for j in range(col):
        print(b[i][j], end=" ")
    print()

for i in range(r):
    for j in range(col):
        for k in range(col):
            c[i][j] += a[i][k] * b[k][j]

print("Matrix C (Multiplication Result):")
for i in range(r):
    for j in range(col):
        print(c[i][j], end=" ")
    print()
