def delit(a):
    m = []
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            m.append(i)
            if i != a // i:
                m.append(a // i)
    return sorted(m)


for i in range(862346, 1056243):
    s = delit(i)
    if len(s) > 3:
        sm = sum(s)
        a1 = s[0]
        an = s[-1]
        n = len(s)
        d = ((2*sm / n) - 2*a1) / (n - 1)
        if d == 100:
            print(i, s[-1])
