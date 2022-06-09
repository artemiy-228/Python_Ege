#RUS - Найти числа у которых 6 делителей
#ENG - find numbers with 6 divisors

def count(x):
    s = 0
    for i in range(1, x + 1):
        if x % i == 0:
            s += 1
    return s

for i in range(int(input()), int(input()) + 1):
    if count(i) == 6:
        print(i, end=" ")
