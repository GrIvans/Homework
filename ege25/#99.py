def delitel(a):
    m = []
    n = a**.5
    if n.is_integer():
        for i in range(2, int(n) + 1):
            if a % i == 0:
                if len(str(i)) == 2:
                    m.append(i)
                if a // i != i:
                    if len(str(a // i)) == 2:
                        m.append(a // i)
    return m

#не работает
for i in range(333555, 777999 + 1):
    a = delitel(i)
    if len(a) == 35:
        print(i, min(a), max(a))
