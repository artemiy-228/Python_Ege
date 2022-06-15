#RUS - найдите количество идущих подряд символов, среди которых нет Z
#ENG - find count letters without Z

f = open('EGE_24_01_02.txt')

line = f.readline()
k = 0
max = 0
for i in range(len(line) - 1):
    if line[i] != "Z":
        k += 1
        if k > max:
            max = k
    else:
        k = 0

print(max)
