#RUS - найдите произведение цифр
#ENG - find multiply of digits

def mult(x):
    s = 1
    while x > 0:
        s *= (x % 10)
        x //= 10
    return s

a = int(input())
b = int(input())

for i in range(a, b + 1):
    if mult(i) > 100:
        print(i, end=" ")
