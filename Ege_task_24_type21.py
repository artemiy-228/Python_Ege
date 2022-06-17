#RUS - найдите количество строк, где буква R встречается чаще буквы F
#ENG - find the count of lines where the letter R occurs more often than the letter F

f = open("EGE_24_06_02.txt")

k = 0
for line in f:
    if line.count("R") > line.count("F"):
        k += 1



print(k)
