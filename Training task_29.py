#RUS - рекурсия
#ENG - recursion


def f(n):
    if n > 35:
        return n * n + 5 * n + 4
    if n <= 35 and n % 2 == 0:
        return f(n + 1) + 3 * f(n + 6)
    return f(n + 2) + f(n + 6)

def digitsum(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s


k = 0
