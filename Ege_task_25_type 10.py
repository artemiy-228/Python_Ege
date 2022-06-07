#RUS - Среди промежутка найти те числа, у которых сумма цифр кратна 11, произведение цифр кратно трем и не равно 0
#ENG - Among the interval find numbers whose sum of digits is divisible by 11, multiplication of digits is divisible by 3 and not equal to 0

def digit_sum(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

def digit_prod(x):
    s = 1
    while x > 0:
        s *= x % 10
        x //= 10
    return s






for i in range(33465, 33484):
    if digit_sum(i) % 11 == 0 and digit_prod(i) % 3 == 0 and digit_prod(i) != 0:
        print(digit_sum(i), digit_prod(i))
