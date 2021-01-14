def prost(a):
    n = int(a**.5)
    for i in range(2, n + 1):
        if a % i == 0:
            return False
    return True

#не работает
def delit(a):
    n = int(a**.5)
    m = []
    for i in range(1, n + 1):
        if a % i == 0 and i != 1 and prost(i):
            m.append(i)
            if a // i != i and prost(a // i):
                m.append(a // i)
    return m


k = 0
for i in range(2, 20001):
    a = delit(i)
    if len(a) > 3:
        k += 1
print(k)
