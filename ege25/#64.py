def f(a):
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            return False
    return True

k = 1
for i in range(2532000, 2532160 + 1):
    if f(i) and i % 10 == 7:
        print(k, i)
        k += 1
