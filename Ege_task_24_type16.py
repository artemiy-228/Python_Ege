#RUS - найдите количество букв рядом с которыми есть буква R
#ENG - find count letters nearby letter R

f = open("EGE_24_05_20.txt")


line = f.readline()
k = 0
for i in range(1, len(line) - 1):
    if line[i-1] == "R" or line[i+1] == "R":
        k += 1

if line[0:2] == "RR":
    k += 1
if line[-2:] == "RR":
    k += 1

print(k)
