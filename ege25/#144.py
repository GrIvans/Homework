def prost(a):
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            return False
    return True

def delit(a):
    m = []
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            if i != a // i and prost(i) and (a // i):
                m.append(i)
                m.append(a // i)
    return m


for i in range(33333, 55556):
    sm = sum(delit(i))
    if sm != 0:
        if i % sm == 0 and sm > 250:
            print(i, sm)
            