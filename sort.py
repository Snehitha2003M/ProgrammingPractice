a=[2,9,3,8,4,7,5,6]
n=len(a)
x=1
i=1
for i in range(0,n-1):
    j=x
    for j in range(x,n):
       # print(i,j)
        if (a[i]>a[j]):
            t=a[i]
            a[i]=a[j]
            a[j]=t
    x=x+1
print(a)