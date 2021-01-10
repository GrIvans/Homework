def f(a):
    m = []
    n = (a**0.5)
    if n.is_integer():
        for i in range(1, a + 1):
            if a % i == 0:
                m.append(i)
    return sorted(m)


for i in range(11275, 16328 + 1):
    a = f(i)
    if len(a) == 5:
        print(*a)
