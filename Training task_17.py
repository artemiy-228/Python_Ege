min1 = 101
min2 = 101
i1 = 0
i2 = 0
for i in range(1, 11):
    a = int(input())
    if a < min1:
        min2 = min1
        i2 = i1
        i1 = i
        min1 = a
    elif a < min2 and a > min1:
        i2 = i
        min2 = a

print(i1,i2, sep="\n")
