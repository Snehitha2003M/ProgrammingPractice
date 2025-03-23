n = 5
for i in range(n):
    # First part: Print numbers from 1 to (n - i)
    for j in range(1, n - i + 1):
        print(j, end="")

    # Middle spaces: Print (2 * i) spaces (corrected)
    print(" " * (2 * i), end="")

    # Second part: Print numbers from (n - i) down to 1
    for j in range(n-i, 0, -1):  # Remove condition to avoid skipping first row
        print(j, end="")

    print()  # Move to the next line
