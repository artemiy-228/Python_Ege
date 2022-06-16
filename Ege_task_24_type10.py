#RUS - найдите сколько раз в строке встречается английская буква "A" между двуми разными цифрами
#ENG - find count letter A beetween different numbers


f = open('EGE_24_03_29.txt')

line = f.readline()

k = 0
max = 0
for i in range(1, len(line) - 1):
    if line[i - 1].isdigit() and line[i + 1].isdigit() and line[i] == "A" and line[i + 1] != line[i - 1]:
        k += 1
        if k > max:
            max = k




print(max)
