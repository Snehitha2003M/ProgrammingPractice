def factorial(n):
    fact = 1  # Initialize factorial as 1
    for i in range(1, n + 1):
        fact *= i  # Multiply current number to factorial
    return fact  # Return factorial of n

n = int(input("Enter a number: "))
s = 0  # Initialize sum

for i in range(1, n + 1):  
    s = s + factorial(i + 1) // factorial(i)  

print("Sum of the series:", s)
