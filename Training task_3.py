N = 8

max = int(input())

for i in range(N - 1):
    a = int(input())
    if [a > max, a % 7 == 0].count(True) == 2:
        max = a

print(max)
