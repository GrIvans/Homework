def prost(a):
    for i in range(2, int(a**.5) + 1):
        if a % 2 == 0:
            return False
    return True


def delit(a):
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            if i != a // i and prost(i) and prost(a // i):
                if i % 10 == (a // i) % 10:
                    return True
    return False


mx = 0
k = 0
for i in range(237981, 309877):
    if delit(i):
        k += 1
        mx = i
print(k, mx)
