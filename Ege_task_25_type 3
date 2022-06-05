# IT science exam num 25

for x in range(320266, 320277):
    d = 1
    k = 0
    list = []
    while d * d < x:
        if x % d == 0:
            if d % 2 != 0:
                list.append(d)
                k += 1
            if x // d % 2 != 0:
                list.append(x // d)
                k += 1
        d += 1
    if d * d == x:
        if d % 2 != 0:
            list.append(d)
            k += 1
    if k == 4:
        print(sorted(list))
