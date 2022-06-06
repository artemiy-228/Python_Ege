def digitSum(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s


N = 8

min = 30  # the largest sum of digits of a three-digit number is 27
num = 1000

for i in range(N):
    a = int(input())
    if digitSum(a) < min:
        min = digitSum(a)
        num = a

print(num)
