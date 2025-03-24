
a=[2,3,4,5,2,3,7,8,4,9,5]
n=len(a)
x=1
print(a)
for i in range(n+1):
    for j in range(x,n):
        if (a[i]==a[j]):
            print(a[i],"is a duplicate")
            a[j]=0
    x=x+1
print(a)