def sover(a):
    n = int(a**.5)
    m = []
    for i in range(1, n + 1):
        if a % i == 0:
            m.append(i)
            if a // i != i and a // i != a:
                m.append(a // i)
    if sum(m) == a:
        return (True, len(m))
    return (False, len(m))


for i in range(2, 10001):
    a = sover(i)
    if a[0]:
        print(i, a[1])
