def delitel(a):
    m = []
    n = (a**.5)
    if n.is_integer():
        for i in range(2, int(n) + 1):
            if a % i == 0:
                m.append(i)
                if a // i != i:
                    m.append(a // i)
    return m


for i in range(81234, 134689 + 1):
    a = delitel(i)
    if len(a) == 3:
        print(min(a), max(a))
