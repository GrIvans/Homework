def delit(a):
    n = a**.5
    k = 0
    if n.is_integer():
        for i in range(2, int(n) + 1):
            if a % i == 0:
                k += 1
                if a // i != i:
                    k += 1
    return k


k = 0
for i in range(3661, 33625 + 1):
    if delit(i) == 1:
        k += 1
print(k)
