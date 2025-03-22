def is_prime(n):
    fc = 0  # Factor count

    for i in range(1, n + 1):  # Loop from 1 to n
        if n % i == 0:  # If i is a factor of n
            fc = fc + 1  

    if fc > 2:  
        return 0 #print(n, "Not a Prime")
    else:  
        return n # print(n, "Is Prime")
n=int(input("Enter the n "))
for i in range(1,n+1):
    result=is_prime(i)
    if (result==i):
        print(i)