def is_prime(n):
    fc = 0  # Factor count

    for i in range(1, n + 1):  # Loop from 1 to n
        if n % i == 0:  # If i is a factor of n
            fc = fc + 1  

    if fc > 2:
        print(n, "Not a Prime")#return 0
    else:  
        print(n, "Is Prime")#return n 

def main():
    a=int(input("Enter the value: "))
    b=is_prime(a)

if __name__=="__main__":
    main()
    