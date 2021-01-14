def nedost(a):
    n = int(a**.5)
    m = []
    for i in range(1, n + 1):
        if a % i == 0:
            m.append(i)
            if a // i != i and a // i != a:
                m.append(a // i)
    if sum(m) < a:
        return True
    return False


k = 0

for i in range(2, 30001):
    if nedost(i):
        k += 1
print(k)
