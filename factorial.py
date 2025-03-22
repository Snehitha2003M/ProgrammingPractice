#n! = n × (n-1) × (n-2) × ... × 1
n = int(input("Enter n: "))
fact = 1

for i in range(1, n + 1):
    fact =fact * i

print("Factorial of", n, "is:", fact)
