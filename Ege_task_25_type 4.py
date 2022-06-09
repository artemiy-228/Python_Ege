# IT science exam num 25

def divcount(x):         # define function to calculate divisor count. We work with odd numbers only.
    d = 1
    list = []
    while d * d < x:
        if x % d == 0:
            list.append(d)
            list.append(x // d)
        d += 2
    if d * d == x:
        list.append(d)
    return list



for i in range(174931, 174949, 2):  #step by 2 cause we need to found only odd numbers. Even numbers has a even divisors
    if len(divcount(i)) == 4:
        print(divcount(i))
