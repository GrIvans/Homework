def f(x):
    n = int(x**0.5)
    m = []
    for i in range(1, n + 1):
        if x % i == 0 and i % 2 == 0:
            m.append(i)
        if x % i == 0 and (x // i) % 2 == 0:        
            m.append(x // i)
    return sorted(m, reverse=1)


for i in range(190201, 190280 + 1):
    a = f(i)
    if len(a) == 4:
        print(*a)
