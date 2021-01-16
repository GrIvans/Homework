def delit(a):
    k = 0
    n = a**.5
    if n.is_integer():
        for i in range(2, int(n) + 1):
            if a % i == 0:
                k += 1
                if a // i != i:
                    k += 1
    if k == 1:
        return True
    return False

def summaCifr(a):
    sm = 0
    while a != 0:
        sm += a % 10
        a //= 10
    return sm


sm = 0
for i in range(4099, 26985 + 1):
    if delit(i):
        sm += summaCifr(i)
print(sm)
