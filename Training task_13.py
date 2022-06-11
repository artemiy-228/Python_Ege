N = 10

min1 = 1001
min2 = 1002

for i in range(N):
    a = int(input())
    if a < min1:
        min2 = min1
        min1 = a
    elif a < min2:
        min2 = a

print(min1, min2, sep="\n")
