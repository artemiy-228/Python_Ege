N = 10

min = 59050
s = 0
max = 1


def multdigit(n):
    s = 1
    while n > 0:
        s = s * (n % 10)
        n //= 10
    return(s)

for i in range(N):
    a = int(input())
    if multdigit(a) < min:
        min = multdigit(a)
        s = 1
        max = a
    elif multdigit(a) == min:
        s += 1
        if a > max:
            max = a
print(s, max)
