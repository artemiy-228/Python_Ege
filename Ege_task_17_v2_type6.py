#RUS - Найти количество пар, сумма модулей которых попадает в указанный промежуток. И найти максимальное число среди этих пар.
#ENG - Fnd count pairs, which sum of modules in interval [1500;4300]. ANd found bigger element on this pairs


f = open("EGE_17_02.txt")
list = []
for i in f:
    list.append(int(i))


k = 0
max = list[0]


for i in range(len(list) - 1):
    a = list[i]
    b = list[i + 1]
    if 1500 <= abs(a) + abs(b) <= 4300:
        k += 1
        if a > b and a > max:
            max = a
        elif b > a and b > max:
            max = b




print(k, max)




#THIS TASK TYPE 2
#RUS - Найти количество пар, модуль суммы которых попадает в указанный промежуток. И найти максимальное число среди этих пар.
#ENG - Fnd count pairs, which modules summ in interval [1500;4300]. ANd found bigger element on this pairs


f = open("EGE_17_02.txt")
list = []
for i in f:
    list.append(int(i))


k = 0
max = list[0]


for i in range(len(list) - 1):
    a = list[i]
    b = list[i + 1]
    if 1400 <= abs(a + b) <= 4900:
        k += 1
        if a > b and a > max:
            max = a
        elif b > a and b > max:
            max = b




print(k, max)





