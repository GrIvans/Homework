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
                return (a // i - i)
    return -1


mx = 0
m = 0
k = 0
for i in range(238941, 315676):
    s = delit(i)
    if s != -1:
        k += 1
        if s > mx:
            m = i
            mx = s
print(k, mx)
