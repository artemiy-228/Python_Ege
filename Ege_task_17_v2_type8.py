#RUS - Найдите количество пар чисел, квадрат суммы которых не превышает указанное число.Потом найдите их максимальную сумму и ее минимальный элемент
#ENG - Find count of pairs, where squares sum lower than number. After this find maximal sum and her smaller element


f = open("EGE_17_02.txt")
list = []
for i in f:
    list.append(int(i))


k = 0
max = -200001
asnwer = 0

for i in range(len(list) - 1):
    a = list[i]
    b = list[i + 1]
    if (a + b) ** 2 <= 218000 and ((a + b) ** 2) % 2 != 0:
        k += 1
        if a + b > max:
            max = a + b
            if a > b:
                answer = b
            else:
                answer = a




print(k, answer)


