#RUS - Программа перебирает числа и ищет сумму простых делителей каждого числа.
#ENG - The program recalculates the number and calculates the number of prime divisors of each number.

def isSimple(x):
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

def sumsimplediv(x):
    s = 0
    d = 2
    while d * d < x:
        if x % d == 0:
            if isSimple(d):
                s += d
            if isSimple(x // d):
                s += x // d
        d += 1
    if d * d == x:
        if isSimple(d):
            s += d
    return s

num = 750001
k = 0

while k < 5:
    if sumsimplediv(num) % 10 == 3:
        print(num, sumsimplediv(num))
        k += 1
    num += 1
