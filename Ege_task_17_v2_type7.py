#RUS - Найти количество пар, где сумма квадратов больше указанного числа. А потом найти минимальную сумму и ее максимальный элемент.
#ENG - Find count of pairs, where sum of squares bigger than number. After this find minimal sum and her bigger element


f = open("EGE_17_02.txt")
list = []
for i in f:
    list.append(int(i))


k = 0
min = 200001
asnwer = 0

for i in range(len(list) - 1):
    a = list[i]
    b = list[i + 1]
    if a ** 2 + b ** 2 > 141000 and (a ** 2 + b ** 2) % 2 == 0:
        k += 1
        if a + b < min:
            min = a + b
            if a > b:
                answer = a
            else:
                answer = b




print(k, answer)


