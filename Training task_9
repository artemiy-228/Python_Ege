def digitSum(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s


N = 8

max = 1  # the smallest sum of digits of a three-digit number is 1
num = 0

for i in range(N):
    a = int(input())
    if max <= digitSum(a) and a > num:
        max = digitSum(a)
        num = a

print(num)
