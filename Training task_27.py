#RUS - Вывести в столбик все числа меньшие n, квадрат суммы цифр которых равен m
def sum(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

n = int(input())
m = int(input())

for i in range(1, n):
    if sum(i) ** 2 == m:
        print(i)
