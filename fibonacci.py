#F(n)=F(n−1)+F(n−2)
n = 5

a, b = 0, 1
sum_fib = 0

for _ in range(n):
    sum_fib += a
    a, b = b, a + b

print("Sum of first", n, "Fibonacci numbers:", sum_fib)
