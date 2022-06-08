#RUS - Найдите количество пар, где оба числа оканчиваются на нечетные, неравные цифры и хотя бы 1 число больше указанного. Потом найдите модуль минимального произведения.
#ENG - Find the count of pairs where both numbers end in odd, unequal digits and at least 1 number greater than the specified one. Then find the modulus of the minimum multiply.


f = open("EGE_17_02.txt")
list = []
for i in f:
    list.append(int(i))


k = 0
min = 10000 ** 2

for i in range(len(list) - 1):
    a = list[i]
    b = list[i + 1]
    if abs(a) % 2 != 0 and abs(b) % 2 != 0 and abs(a) % 10 != abs(b) % 10 and [a > -3200, b > -3200].count(True) >= 1:
        k += 1
        if abs(a * b) < min:
            min = abs(a * b)


print(k, min)
