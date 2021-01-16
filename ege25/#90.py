def delit(a):
    k = 0
    n = int(a**.5)
    for i in range(2, n + 1):
        if a % i == 0:
            k += 1
            if a // i != i:
                k += 1
    if k == 2:
        return True
    return False


for i in range(3594, 21891 + 1):
    if delit(i):
        mx = i
print(mx)
