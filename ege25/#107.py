def prost(a):
    if a == 2:
        return True
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            return False
    return True


def delit(a):
    mn = 100001
    m = 0
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            if prost(i) and prost(a // i) and a != a // i:
                if a // i - i < mn:
                    mn = a // i - i
                    m = abs(i - a // i)
    return m


def kostil(a):
    mn = 100001
    m = 0
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            if prost(i) and prost(a // i) and a != a // i:
                return True
    return False


mn = 10001
m = 0
k = 0
for i in range(153732, 225675):
    s = delit(i)
    if s > 0:
        if s < mn:
            mn = s
            m = i
    if kostil(i):
        k += 1
print(k, m)
