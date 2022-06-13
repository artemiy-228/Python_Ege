#ENG - found number

for s0 in range(1, 1000):
    s = s0
    n = 34
    while s < 2640:
        s = s * 2
        n = n + 4
    if n == 62:
        print(s0)
