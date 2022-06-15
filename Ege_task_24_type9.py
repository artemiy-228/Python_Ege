#RUS - найдите количество элементов, где 2 соседних элемента не могут быть одинаковыми
#ENG - find the number of elements where 2 adjacent elements cannot be the same

f = open('EGE_24_03_15.txt')

line = f.readline()

k = 1
max = 1
for i in range(len(line) - 1):
    if (line[i + 1].isalpha() and line[i].isdigit()) or (line[i].isalpha() and line[i + 1].isdigit()):
        k += 1

        if k > max:
            max = k
    else:
        k = 1

print(max)
