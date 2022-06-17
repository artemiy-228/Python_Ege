#RUS - сложное условие
#ENG - each next letter depends on the previous one

f = open("EGE_24_04_15.txt")
a = f.readline()
k = 0
max = 0

for i in range(len(a) - 2):
    if a[i] in "abcd" and a[i + 1] != a[i] and a[i + 1] in "cde" and a[i + 2] in "bce" and a[i + 2] > a[i] and a[i + 3] in a[i:i + 3]:
        k += 1
        if k > max:
            max = k
print(max)

