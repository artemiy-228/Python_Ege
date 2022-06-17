#RUS - найдите какой символ стоящий перед R, встречается чаще всего.
#ENG - Find out which character before R is the most common.

f = open("EGE_24_05_15.txt")

list = [0] * 26
line = f.readline()
list1 = []


for i in range(1, len(line)):
    if line[i] == "R":
        list[ord(line[i - 1]) - 65] += 1
        
        
for i in range(26):
    print(chr(65 + i), "-", list[i])
