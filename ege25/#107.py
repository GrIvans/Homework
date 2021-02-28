def prost(a):
    if a == 2:
        return True
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            return False
    return True


def delit(a):
    mn = 100001
    m = ()
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            if prost(i) and prost(a // i) and a != a // i:
                if a // i - i < mn:
                    mn = a // i - i
                    m = abs(i - a // i)
    return m


mn = 10001
m = 0
k = 0
for i in range(153732, 225675):
    s = delit(i)
    if s != 100001:
        k += 1
        if m < mn:
            mn = m
            m = i
print(k, m)
