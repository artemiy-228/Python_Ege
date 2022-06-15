#RUS - определите количество идущих подряд различных чисел
#ENG - find count the number of different numbers in a row

f = open('EGE_24_02_06.txt')

line = f.readline()
k = 1
max = 1
for i in range(len(line) - 1):
    if line[i] != line[i + 1]:
        k += 1
        if k > max:
            max = k
    else:
        k = 1

print(max)
