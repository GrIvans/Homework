def f(a):
    n = int(a**0.5)
    m = []
    for i in range(1, n):
        if a % i == 0:
            m.append(i)
            m.append(a // i)
    return m

for i in range(126849, 126872):
    m = f(i)
    if len(m) == 4:
        print(*sorted(m))
