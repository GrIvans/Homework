def f(a):
    n = (a**.5)
    m = [1, 2]
    if n.is_integer():
        for i in range(1, int(n) + 1):
            if a % i == 0:
                m.append(i)
                if a // i != i:
                    m.append(a // i)
    return (len(m), a, (sorted(m))[-1])
#неверно
k = 1
for i in range(194441, 196500 + 1):
    a = f(i)
    if a[0] % 2 == 1:
        print(k, *a)
        k += 1