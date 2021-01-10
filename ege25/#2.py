def f(a):
    n = int(a**0.5)
    m = []
    for i in range(1, n):
        if a % i == 0:
            m.append(i)
            m.append(a // i)
    return m

m = []
for i in range(102714, 102726):
    a = f(i)
    if len(a) == 4:
        print(*sorted(a))