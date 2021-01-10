def f(a):
    m = []
    if (a**.5).is_integer():
        for i in range(1, a + 1):
            if a % i == 0:
                m.append(i)
    return sorted(m)


for i in range(20789, 35672 + 1):
    a = f(i)
    if len(a) == 5:
        print(*a)
