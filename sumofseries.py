def factorial(n):
    fact = 1  # Initialize factorial as 1
    sum_is=0
    for i in range(1, n + 1):
        fact *= i # Multiply current number to factorial
        sum_is+=fact
        print(f"{i}! = {fact}")  # Print factorial of i
    print(sum_is)
n = int(input("Enter a number: "))
result=factorial(n)