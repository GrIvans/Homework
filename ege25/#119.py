def prost(a):
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            return False
    return True


def delit(a):
    k = 0
    n = a**.5
    if n.is_integer():
        for i in range(2, int(a**.5) + 1):
            if a % i == 0:
                k += 1
                if a // i != i:
                    k += 1
    return k


a = []
for i in range(236228, 305284):
    s = delit(i)
    if s == 3:
        a.append(i)
print(len(a), sum(a)/len(a))
