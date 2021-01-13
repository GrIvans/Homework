def f(a):
    n = int(a**0.5)
    m = []
    for i in range(1, n + 1):
        if a % i == 0:
            m.append(i)
            if a // i != i:
                m.append(a // i)
    return (len(m), a, sorted(m, reverse=1))


dMin = ()
mxLen = 0
for i in range(394441, 394505 + 1):
    a = f(i)
    if a[0] > mxLen:
        dMin = a
        mxLen = a[0]

print(dMin[0], *dMin[2][:2])
