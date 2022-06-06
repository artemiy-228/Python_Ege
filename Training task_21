def sum(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s
    
max = 0
c = 0


for i in range(10):
    a = int(input())
    if sum(a) > max:
        max = sum(a)
        c = 1
    elif sum(a) == max:
        c += 1
        
        
print(c)
