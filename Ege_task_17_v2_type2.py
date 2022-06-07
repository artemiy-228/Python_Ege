#RUS - Отличается от прошлой, что у нас есть возможность искать по другому условию(деление на 52)
#ENG - It differs previous task in that we have the ability to search by a different condition (divided by 52)



f = open("EGE_17_02.txt")
list = []

for i in f:
    list.append(int(i))

def isSqrt(x):
    if x < 0:
        return False
    s = int(x ** 0.5)
    if s ** 2 == x or (s + 1) ** 2 == x:
        return True
    return False



k = 0
max = -200001
for i in range(len(list) - 1):
    if isSqrt(list[i]) or isSqrt(list[i + 1]) or list[i] % 52 == 0 or list[i + 1] % 52 == 0:
        k += 1
        if list[i] + list[i+1] > max:
            max = list[i] + list[i+1]

print(k, max)
