def is_prime(n):
    fc = 0  # Factor count

    for i in range(1, n + 1):  # Loop from 1 to n
        if n % i == 0:  # If i is a factor of n
            fc = fc + 1  

    if fc > 2:  
        return 0 #print(n, "Not a Prime")
    else:  
        return n # print(n, "Is Prime")

a = 11  
is_prime(a)# Check for 11 
result=is_prime(a)
print(a,result)
if result==a:
    print("it is prime")
else:
    print("Not a prime")
result=is_prime(25)  # Check for 25  
print(25, result)
if result==25:
    print("it is prime")
else:
    print("Not a prime")
