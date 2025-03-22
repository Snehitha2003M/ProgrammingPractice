a=626
c=0

c=(c*10)+(a%10)
a=int(a/10)

c=(c*10)+(a%10)
a=int(a/10)

c=(c*10)+(a%10)
a=int(a/10)

print("Yes, because reverse of 626 is also 626: ",c)