N = int(input())


max1 = 0
max2 = 0
s1 = 0
s2 = 0

for i in range(N):
    a = int(input())
    if a > max1:
        max2 = max1
        s2 = s1
        max1 = a
        s1 = 1
    elif a == max1:
        s1 += 1
    elif a > max2:
        max2 = a
        s2 = 1
    elif a == max2:
        s2 += 1
print(s1, s2)
