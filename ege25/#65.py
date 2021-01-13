def f(a):
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            return False
    return True

d = []
for i in range(2532000, 2532160 + 1):
    if f(i):
        d.append(i)

for i in range(0, len(d), 3):
    print(i + 1, d[i])
