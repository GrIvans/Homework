def sover(a):
    n = int(a**.5)
    m = []
    for i in range(1, n + 1):
        if a % i == 0:
            m.append(i)
            if a // i != i:
                m.append(a // i)
    return m


for i in range(2, 263001):
    a = sover(i)
    b = sover(sum(a))
    if (sum(b) // 2) == i and sum(b) % 2 == 0:
        print(i)
