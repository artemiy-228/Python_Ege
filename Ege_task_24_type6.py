#RUS - определите количество подряд идущих цифр, где каждое следующее убывает
#ENG - a certain number of consecutive digits, where a specific one decreases

f = open('EGE_24_02_10.txt')

line = f.readline()
k = 1
max = 1
for i in range(len(line) - 1):
    if line[i] < line[i + 1]:
        k += 1
        if k > max:
            max = k
    else:
        k = 1

print(max)

