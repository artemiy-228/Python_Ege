#RUS - определите количество идущих подряд одинаковых чисел
#ENG - find count the number of identical numbers in a row

f = open('EGE_24_02_03.txt')

line = f.readline()
k = 1
max = 1
for i in range(len(line) - 1):
    if line[i] == line[i + 1]:
        k += 1
        if k > max:
            max = k
    else:
        k = 1

print(max)
