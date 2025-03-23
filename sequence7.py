n=5
for i in range(n):
    for j in range(1,i+1):
        print(j,end='')
    print(" "*2*(n-i),end="")
    for j in range(i,0,-1):
        print(j,end="")
    print()