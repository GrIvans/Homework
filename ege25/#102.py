def prost(a):
    if a == 2:
        return True
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            return False
    return True


def deletel(a):
    n = int(a**.5)
    for i in range(2, n + 1):
        if a % i == 0:
            if i != a // i and prost(i) and prost(a // i):
                return True
    return False


k = 0
for i in range(268312, 336493):
    if deletel(i):
        k += 1
        if k == 1:
            mn = i
print(k, mn)
