#RUS - определите количество идущих подряд цифр где нет 444
#ENG - find the number of consecutive digits where no 444

f = open("EGE_24_02_15.txt")

list = f.readline()
k = 1
max = 1
for i in range(1, len(list) - 1):
    if list[i - 1: i + 2] != "444":
        k += 1
        if k > max:
            max = k
    elif list[i - 1: i + 2] == "444":
        k = 2
print(max)
