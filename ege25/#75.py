def sov(a):
    n = int(a**.5)
    m = [1]
    for i in range(2, n + 1):
        if a % i == 0:
            m.append(i)
            if a // i != i:
                m.append(a // i)
    if a - sum(m) == 1:
        return True
    return False


for i in range(1000, 20001):
    if sov(i):
        print(i)