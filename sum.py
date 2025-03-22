a=426
c=a%10 #which extracts the last digit=6
a=int(a/10) # // #then it will remove last digit a=426

b=a%10 
a= int(a/10) #//
sum_digits=a+b+c
print(f"{a}+{b}+{c}={sum_digits}")