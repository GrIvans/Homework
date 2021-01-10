def f(a):
    m = []
    if (a**0.5).is_integer():
        for i in range(1, a + 1):
            if a % i == 0:
                m.append(i)
    return m


for i in range(78920, 92430 + 1):
    a = f(i)
    if len(a) == 5:
        print(*sorted(a))
