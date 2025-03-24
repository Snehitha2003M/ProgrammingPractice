r=3
col=3
a=  [
        [2 ,5 ,6 ],
        [1 ,8 ,4 ],
        [3 ,7 ,0 ]
    ]

b=  [
        [3 ,5 ,6 ],
        [4 ,6 ,8 ],
        [7 ,6 ,0 ]
    ]
c=  [
        [0 ,0 ,0 ],
        [0 ,0 ,0 ],
        [0 ,0 ,0 ]
    ]

print("a")
for i in range(0,r):
    for j in range(0,col):
        print(a[i][j],end="")
    print()
print("b")
for i in range(0,r):
    for j in range(0,col):
        print(b[i][j],end="")
    print()
print("c")
for i in range(0,r):
    for j in range(0,col):
        print(c[i][j],end="")
    print()
for i in range(0,r):
    for j in range(0,col):
        c[i][j]=a[i][j]+b[i][j]
        print(c[i][j],end=" ")
    print()