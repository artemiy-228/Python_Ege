N = 6

list = []
max = 0
for i in range(N):
    list.append(int(input()))

for i in range(N):
    if [list[i] > max, list[i] % 7 == 0].count(True) == 2:
        max = list[i]
    if i == 5 and max != 0:
        print(max)
    elif i == 5 and max == 0:
        print("no")
