#ENG - found number



for n0 in range(1, 1000):
    n = n0
    s = 700
    while s - n > 0:
        s -= 60
        n -= 15
    if s == 100:
        print(n0)
