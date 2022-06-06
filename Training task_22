def mult(x):
    s = 1
    while x > 0:
        s *= x % 10
        x //= 10
    return s
    
    
min = 99999
c = 0


for i in range(10):
    a = int(input())
    if mult(a) < min:
        min = mult(a)
        c = 1
    elif mult(a) == min:
        c += 1
        
print(c)
