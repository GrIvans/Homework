def f(a):
    n = int(a**.5)
    m = []
    for i in range(1, n + 1):
        if a % i == 0:
            m.append(i)
            if a // i != i:
                m.append(a // i)
    return (len(m), sorted(m, reverse=1))

mxChislo, mnChislo = (), ()
mxDel = 0
for i in range(586132, 586430 + 1):
    a = f(i)
    if mxDel < a[0]:
        mxDel = a[0]
        mnChislo = a
    if mxDel <= a[0]:
        mxDel = a[0]
        mxChislo = a
print(mnChislo[0], *mnChislo[1][:2])
print(mxChislo[0], *mxChislo[1][:2])
