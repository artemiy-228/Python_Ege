#RUS - Среди интервала в файле найти те пары, где хотя бы 1 число является квадратом натурального числа(пара - 2 соседних числа).
#ENG - Among the interval in the file, find those pairs where at least 1 number is the square of natural numbers (pair - 2 accumulated numbers)


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
min = 20001
for i in range(len(list) - 1):
    if isSqrt(list[i]) or isSqrt(list[i + 1]):
        k += 1
        if list[i] + list[i+1] < min:
            min = list[i] + list[i + 1]

print(k, min)
