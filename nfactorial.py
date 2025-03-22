def factorial(n):
    fact = 1  # Initialize factorial as 1

    for i in range(1, n + 1):
        fact *= i  # Multiply current number to factorial
        print(f"{i}! = {fact}")  # Print factorial of i
n = int(input("Enter a number: "))
result=factorial(n)

