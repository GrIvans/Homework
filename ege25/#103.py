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


s = 0
k = 0
for i in range(351627, 428764):
    if deletel(i):
        k += 1
        s += i
print(k, int(s / k))
