def f(a):
    n = int(a**.5)
    m = []
    for i in range(1, n + 1):
        if a % i == 0 and i % 2 == 1:
            m.append(i)
        if a % i == 0 and (a // i) % 2 == 1:
            m.append(a // i)
    return m


for i in range(190061, 190080 + 1):
    a = f(i)
    if len(a) == 4:
        print(*sorted(a, reverse=1))
