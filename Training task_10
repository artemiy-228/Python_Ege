def SepSum(x):
    s = 0
    d = 2
    while d * d < x:
        if x % d == 0:
            s += d
            s += x // d
        d += 1
    return s

a = int(input())
b = int(input())

max = 0
Num = 0

for i in range(a, b + 1):
    if SepSum(i) >= Num:
        Num = SepSum(i)
        max = i

print(max)
