row = 5
col = 5
a = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

n = 5
print("A")
for i in range(row):
    for j in range(col):
        print(a[i][j], end="")
    print()

row = 0
col = n // 2  

for i in range(1, n * n + 1):  
    a[row][col] = i  

    prev_row, prev_col = row, col  
    row -= 1  
    col += 1  

    if row < 0 and col > n - 1:  
        row = prev_row + 1  
        col = prev_col  
    elif row < 0:  
        row = n - 1  
    elif col > n - 1:  
        col = 0  

    if a[row][col] != 0:  
        row = prev_row + 1  
        col = prev_col  

print("\nMagic Square:")
for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")
    print()
