max1 = 100
max2 = 100
max3 = 100

for i in range(10):
    a = int(input())
    if a > max1:
        max3 = max2
        max2 = max1
        max1 = a
    elif a > max2:
        max3 = max2
        max2 = a
    elif a > max3:
        max3 = a

print(max1, max2, max3)
