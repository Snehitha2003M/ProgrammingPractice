a=[2,3,4,5,2,3,7,8,4,9,5]
print(a)
i = 0
n = len(a)
x = 1
j = 1

while (i < n - 1):
    j = x
    while (j < n):
        if a[i] == a[j]:
            print(a[j], "Is duplicate")
            del(a[j])
            n = n - 1
        j = j + 1
    i = i + 1
    x = x + 1

print(a)
    