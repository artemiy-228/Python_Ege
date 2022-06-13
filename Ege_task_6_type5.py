#ENG - found number



for s0 in range(1, 10000):
    s = s0
    n = 5
    while s // n > 0:
        s = s - 6
        n = n + 5
    if n == 35:
        print(s0)
