def f(a):
    n = int(a**.5)
    m = []
    for i in range(1, n + 1):
        if a % i == 0:
            m.append(i)
            if a // i != i:
                m.append(a // i)
    return m

ans = []
mnDel = 10000000001
for i in range(573213, 575340 + 1):
    a = f(i)
    if len(a) == 4:
        if mnDel > sum(a):
            ans = a
            mnDel = sum(a)
print(sum(ans), len(ans), sorted(ans, reverse=True))
