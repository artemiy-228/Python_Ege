#RUS - найдите количество идущих в алфавитном порядке символов.
#ENG - find count letter going in alphabetical order

f = open('EGE_24_01_13.txt')

line = f.readline()
k = 1
max = 1
for i in range(1, len(line)):
    if line[i] >= line[i - 1]:
        k += 1
        if k > max:
            max = k
    else:
        k = 1
print(max)
