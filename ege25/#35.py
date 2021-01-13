def f(a):
    n = int(a**.5)
    m = []
    for i in range(1, n + 1):
        if a % i == 0:
            m.append(i)
            if a // i != i:
                m.append(a // i)
    return(len(m), a, sorted(m, reverse=1)[:2])

d = []
for i in range(394480, 394540 + 1):
    d.append(f(i))
d.sort(reverse=1)
k = 1
for i in reversed(d):
    if i[0] == d[0][0]:
        print(k, i[0], *i[2])
        k += 1