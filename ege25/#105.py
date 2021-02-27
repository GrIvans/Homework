def prost(a):
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            return False
    return True


def delit(a):
    n = int(a**.5)
    mn = 100001
    for i in range(1, n + 1):
        if a % i == 0:
            if prost(i) and prost(a // i):
                if mn < a // i - i:
                    mn = a // i - i
    return mn


def dl(a):
    m = []
    for i in range(1, int(a**.5) + 1):
        if a % i == 0:
            m.append(i)
            if a // i != i:
                m.append(a // i)
    return sorted(m)


mnc = []
for i in range(523456, 578926):
    s = delit(i)
    mnc.append((s, i))
mnc.sort()
print(dl(mnc[0][1]))
