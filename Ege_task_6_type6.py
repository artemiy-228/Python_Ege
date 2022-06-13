#ENG - found number


for s0 in range(6, 10000):
    s = s0
    s = (s + 2) // 8
    n = 19
    while s < 1850:
        s = s * 2
        n = n + 3
    if n == 37:
        print(s0)
        break
