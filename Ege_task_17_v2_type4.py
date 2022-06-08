#RUS - Определите количоство пар у которых оба числа оканчиваются на одинаковые четные числа. И найдите максимальное произведение среди этих пар
#ENG - Determine the number of pairs in which both numbers end in the same even number. And find the maximum multiply among these pairs


f = open("EGE_17_02.txt")
list = []
for i in f:
    list.append(int(i))


k = 0
max = -1


for i in range(len(list) - 1):
    if abs(list[i]) % 10 == abs(list[i + 1]) % 10 and abs(list[i] % 2 == 0):
        k += 1
        r = abs(list[i] * list[i + 1])
        if r > max:
            max = r



print(k, max)


