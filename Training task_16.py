max1 = 1
max2 = -1


for i in range(10):
    a = int(input())
    if a % 2 != 0:
        if a > max1:
            max2 = max1
            max1 = a
        elif a > max2:
            max2 = a

print(max1, max2, sep="\n")
