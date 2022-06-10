#RUS - Напишите программу, которая ищет среди указанного промежутка, простые числа, которые оканчиваются на 3
#ENG - Create a program that finds prime numbers ending in 3 among the specified interval.

def isSimple(x):
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True




for i in range(357741, 358066):
    if i % 10 == 3 and isSimple(i):
        print(i)
