def prost(a):
    if a == 2:
        return True
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            return False
    return True


def delit(a):
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            if prost(i) and prost(a // i) and i != a // i:
                return (a, (i, a // i))
    return (0, (0, 0))


m = []
for i in range(631632, 684935):
    s = delit(i)
    if s[0] != 0:
        m.append(s)
m.sort(reverse=1)
for j in m:
    if j[0] != m[0][0]:
        break
    mn = j
print(mn[1])
