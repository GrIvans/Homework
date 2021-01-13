def f(a):
    n = (a**0.5)
    m = []
    if n.is_integer():
        for i in range(1, int(n) + 1):
            if a % i == 0:
                m.append(i)
                if a // i != i:
                    m.append(a // i)
    return m

for i in range(1820348, 2880927 + 1):
    a = f(i)
    if len(a) == 5:
        print(a)
