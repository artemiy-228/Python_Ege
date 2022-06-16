#RUS - найдите количество хороших строк с а и хороших строк с b. хорошие строки - строки, где все элементы различны
#ENG - find the number of good lines with a and good lines with b. good lines - lines where all elements are distinct

f = open("EGE_24_04_30.txt")
list = f.readline()


kA = 0
kB = 0


for i in range(1, len(list) - 1):
    if list[i] != list[i + 1] and list[i] != list[i - 1] and list[i - 1] != list[i + 1]:
        if "a" in list[i - 1: i + 2] and not "b" in list[i - 1: i + 2]:
            kA += 1
        elif "b" in list[i - 1: i + 2] and not "a" in list[i - 1: i + 2]:
            kB += 1
            
            
print(kB - kA)


