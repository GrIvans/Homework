def prost(a):
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            return False
    return True


def delit(a):
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            if i != a // i and prost(i) and prost(a // i):
                return True
    return False


a = []
for i in range(298435, 363249 + 1):
    if delit(i):
        a.append(i)
sr = sum(a) / len(a)

mn = 10001
ans = 0
for i in (a):
    if abs(sr - i) < mn:
        mn = abs(sr - i)
        ans = i
print(len(a), ans)
