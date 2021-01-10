def f(a):
    n = int(a**0.5)
    m = []
    for i in range(1, n + 1):
        if a % i == 0:
            m.append(i)
            m.append(a // i)
    return sorted(m)


for i in range(150750, 150764):
    a = f(i)
    if len(a) == 4:
        print(*a)
