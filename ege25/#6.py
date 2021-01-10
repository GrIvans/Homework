def f(x):
    n = int(x**0.5)
    m = []
    for i in range(1, n + 1):
        if x % i == 0:
            m.append(i)
            m.append(x // i)
    return m


for i in range(251811, 251827):
    a = f(i)
    if len(a) == 4:
        print(*sorted(a))
