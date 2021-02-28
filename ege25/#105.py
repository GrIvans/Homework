def prost(a):
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            return False
    return True


def delit(a):
    n = int(a**.5)
    mn = 100001
    m = ()
    for i in range(1, n + 1):
        if a % i == 0:
            if prost(i) and prost(a // i) and i != a // i:
                if mn > a // i - i:
                    mn = a // i - i
                    m = (i, a // i)
    return (mn, m)


an = []
for i in range(523456, 578926):
    an.append(delit(i))
an.sort()
print(*an[0][1])
