#RUS - Найдите количество чисел в диапазоне у которых по 2 четные цифры.
#ENG - find count numbers in interval with 2 even numbers

def two(x):
    s = 0
    while x > 0:
        if (x % 10) % 2 == 0:
            s += 1
        x //= 10
    return s

a = int(input())
b = int(input())
s = 0
for i in range(a, b + 1):
    if two(i) == 2:
        s += 1

print(s)
