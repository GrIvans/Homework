def f(a):
    n = int(a**.5)
    m = []
    for i in range(1, n + 1):
        if a % i == 0:
            m.append(i)
            if a // i != i:
                m.append(a // i)
    return (len(m), sorted(m, reverse=1))


d = ()
mxDel = 0
for i in range(286564, 287270 + 1):
    a = f(i)
    if mxDel <= a[0]:
        d = a
        mxDel = a[0]
print(d[0], *d[1][:2])
