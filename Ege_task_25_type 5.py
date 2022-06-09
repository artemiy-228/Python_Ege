# IT science exam num 25
def divisor_dif(x):
    d = 2
    while d * d < x:
        if x % d == 0:
            return x // d - d
        d += 1
    return 0
                        #F = divisor_dif - difference beetween the biggest divisor and the smollest divisor

num = 750001

k = 0
while k < 5:
    if [divisor_dif(num) != 0, divisor_dif(num) % 7 == 0].count(True) == 2:
        print(num, divisor_dif(num))
        k += 1
    num += 1
