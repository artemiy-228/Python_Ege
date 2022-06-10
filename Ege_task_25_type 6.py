# IT science exam num 25
def isSimple(x):
    d = 2
    while d * d <= x:
        if x % d == 0:          #found simple numbers
            return False
        d += 1
    return True


def div(x):
    d = 2
    while d * d <= x:
        if x % d == 0:          #found the biggest divisor
            return x // d
        d += 1
    return 0


num = 500001
k = 0


while k < 5:
    if not isSimple(div(num)):
        print(num, div(num))
        k += 1
    num += 1
