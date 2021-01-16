def summa(a):
    sm = 0
    while a != 0:
        sm += a % 10
        a //= 10
    return sm


def prozv(a):
    p = 1
    while a != 0:
        p *= a % 10
        a //= 10
    if p != 0:
        return p
    return 1


def ansv(a):
    p = 1
    sm = 0
    while a != 0:
        sm += a % 10
        p *= a % 10
        a //= 10
    return(sm, p)


d = []
for i in range(87921, 88187 + 1):
    if prozv(i) % 18 == 0 and summa(i) % 14 == 0:
        d.append(ansv(i))
for i in sorted(d):
    print(*i)
