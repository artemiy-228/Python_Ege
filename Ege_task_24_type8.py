#RUS - найдите количество 200 в строке
#ENG - find count 200 in line

f = open('EGE_24_02_29.txt')

line = f.readline()
print(line.count("200"))


#or u can use this way

f = open('EGE_24_02_29.txt')

line = f.readline()

max = 0
for i in range(2, len(line)):
    if line[i-2:i + 1] == "200":
        k += 1
print(k)
