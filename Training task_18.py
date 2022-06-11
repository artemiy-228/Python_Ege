max1 = 100
max2 = 101

for i in range(10):
    a = int(input())
    if a > 100 and a < 1000:
        if a > max1:
            max2 = max1
            max1 = a
        elif a > max2:
            max2 = a

print(max1, max2)
