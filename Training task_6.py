N = 8
max = 0
min = 1000

for i in range(N):
    x = int(input())
    if x % 2 == 0 and x > max:
        max = x
    elif x % 2 != 0 and x < min:
        min = x
print(max, min)
