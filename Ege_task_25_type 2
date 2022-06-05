# IT science exam num 25

def divcount(x):
    list = []
    d = 2
    while d * d < x:
        if x % d == 0:
            list.append(d)
            list.append(x // d)
        d += 1
    if d * d == x:
        list.append(d)
    return list


for i in range(182486, 182583):
    if len(divcount(i)) == 4:
        print(*divcount(i))
