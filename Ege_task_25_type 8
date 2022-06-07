#RUS - Программа ищет числа, принадлежащие промежутку, которые имеют наибольшее кол-во делителей. Если таких чисел несколько, то выбираем наименьшее. Выводим кол-во делителей, и 2 наибольших
#ENG - Program find number, among interval, which has the most count of divisors.If there are several such numbers, then choose the smallest

def div_count(x):
    s = 2
    d = 2
    while d * d < x:
        if x % d == 0:
            s += 2
        d += 1
    if d * d == x:
        s += 1
    return s
    
    

def bigger_div(x):
    d = 2
    while d * d < x:
        if x % d == 0:
            return x // d
        d += 1
    if d * d == x:
        return d
    return 0
    

max = 0
maxnum = 249423 #maxnum - the bigger divisor in num


for i in range(327075, 327224):
    if div_count(i) > max:
        max = div_count(i)
        maxnum = i
print(max, maxnum, bigger_div(maxnum))
