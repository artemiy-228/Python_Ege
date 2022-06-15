#RUS - Найдите количество нечетных чисел в убывающем порядке
#ENG - Find the number of odd numbers in descending order

f = open('EGE_24_02_24.txt')

line = f.readline()
k = 0
max = 0
if int(line[0]) % 2 != 0:
    k = max = 1

for i in range(1, len(line)):
    if int(line[i]) % 2 == 0:
        k = 0
    elif k == 0:
        k = 1
    elif line[i] <= line[i - 1]:
        k += 1
    else:
        k = 1
    if k > max:
        max = k


print(max)



