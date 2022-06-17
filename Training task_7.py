max = 0
Num = 0

for i in range(10):
    a = int(input())
    if a % 10 > max:
        max = a % 10
        Num = a

print(Num)
