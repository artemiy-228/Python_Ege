#RUS - Найдите количество простых чисел
#ENG - find count simple numbers
def isPrime(x):
    s = 0
    for i in range(1, x + 1):
        if x % i == 0:
            s += 1
    if s == 2:
        return True
    return False




a = int(input())
b = int(input())
s = 0
for i in range(a, b + 1):
    if isPrime(i):
        s += 1
print(s)
