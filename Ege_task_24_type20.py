#RUS - Найдите какой символ встречается чаще всего между 2 одинаковыми символами
#ENG - Which character appears most often between 2 characters

f = open("EGE_24_05_14.txt")


line = f.readline()
list = [0] * 26

for i in range(1, len(line) - 1):
    if line[i - 1] == line[i + 1]:
        list[ord(line[i]) - 65] += 1

for i in range(26):
    print(list[i], chr(65 + i))

print()
