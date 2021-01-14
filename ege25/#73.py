def izb(a):
    m = [1]
    n = int(a**.5)
    for i in range(2, n + 1):
        if a % i == 0:
            m.append(i)
            if a // i != i:
                m.append(a // i)
    if sum(m) > a:
        return True
    return False

k = 0
for i in range(2, 20001):
    if izb(i):
        k += 1
print(k)