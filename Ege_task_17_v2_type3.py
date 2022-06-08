#RUS - Определите количество пар чисел, у которых оба числа оканчиваются на 2 и максимальный модуль разности этих пар
#ENG - Determine the number of pairs of numbers whose both numbers end in 2 and the maximum modulus of the difference of these pairs


f = open("EGE_17_02.txt")
list = []
for i in f:
    list.append(int(i))
    
    
k = 0
max = -1


for i in range(len(list) - 1):
    if abs(list[i]) % 10 == 2 and abs(list[i + 1]) % 10 == 2:
        k += 1
        r = abs(list[i] - list[i + 1])
        if r > max:
            max = r



print(k, max)


