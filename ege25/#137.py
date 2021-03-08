def deliteli(a):
    m = []
    for i in range(2, int(a**5) + 1):
        if a % i == 0 and a // i != i:
            if a // i - i < 110:
                m.append((i, a // i))
    return sorted(m)


for i in range(1000000, 1500001):
    s = deliteli(i)
    if len(s) > 3:
        print(i, s[-1])
