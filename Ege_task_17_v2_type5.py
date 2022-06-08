#RUS - Определите количество пар, у которых оба числа не делятся на 28 и оканчиваются на одинаковую четную цифру. Найдите их наименьшей  модуль произведения
#ENG - Determine the number of pairs in which both numbers are not divisible by 28 and end in the same even digit. Find their smallest modulus of the multiply


f = open("EGE_17_02.txt")
list = []
for i in f:
    list.append(int(i))


k = 0
min = 10000 ** 2


for i in range(len(list) - 1):
    a = abs(list[i])
    b = abs(list[i + 1])
    if a % 10 == b % 10 and a % 2 == 0 and a % 28 != 0 and b % 28 != 0:
        k += 1
        r = abs(a * b)
        if r < min:
            min = r



print(k, min)


