N = 6

min = int(input())

for i in range(N - 1):
    a = int(input())
    if a < min:
        min = a

print(min)
