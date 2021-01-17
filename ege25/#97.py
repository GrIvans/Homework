def deletel(a):
    m = []
    n = int(a**.5)
    for i in range(2, n + 1):
        if a % i == 0:
            m.append(i)
            if a // i != i:
                m.append(a // i)
    return m


for i in range(135790, 163228 + 1):
    a = deletel(i)
    if sum(a) > 460000:
        print(len(a), sum(a))
