#ENG - found number

for s0 in range(1, 10000):
    s = s0
    n = 73
    while s > 0:
        s = s // 2
        n = n - 6
    if n == 13:
        print(s0)
