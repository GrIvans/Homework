def f(a):
    n = (a**0.5)
    m = [1, 2]
    if n.is_integer():
        for i in range(1, int(n) + 1):
            if a % i == 0:
                m.append(i)
                if a // i != i:
                    m.append(a // i)
    return(a, len(m) - 2, m[-1])


k = 1
for i in range(248015, 251575 + 1, 2):
    a = f(i)
    if a[1] % 2 == 1:
        print(k, *a)
        k += 1
