def f(a):
    m = []
    n = int(a**0.5)
    for i in range(1, n + 1):
        if a % i == 0:
            m.append(i)
            m.append(a // i)
    return m


for i in range(193136, 193223 + 1):
    a = f(i)
    if len(a) == 6:
        print(*sorted(a))
