#RUS - найдите количество чисел среди которых нет рядом стоящих 5 и 7  и 5 и 7
#ENG - find the number of numbers among those not adjacent to 5 and 7 and 5 and 7


f = open("EGE_24_02_11.txt")

list = f.readline()
k = 1
max = 1
for i in range(len(list) - 1):
    if not list[i:i + 2] in ["56", "65", "57", "75"]:
        k += 1
        if k > max:
            max = k
    else:
        k = 1

print(max)
