def f(a):
    n = int(a**.5)
    m = []
    for i in range(1, n + 1):
        if a % i == 0:
            m.append(i)
            if a // i != i:
                m.append(a // i)
    return m


mxSum = 0
mxChisl = 0
allDel = []
for i in range(268220, 270335 + 1):
    a = f(i)
    if len(a) <= 4:
        if sum(a) > mxSum:
            mxChisl = i
            mxSum = sum(a)
            allDel = a

print(mxSum, len(allDel), sorted(allDel, reverse=1))
