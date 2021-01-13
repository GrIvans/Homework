def f(a):
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            return False
    return True

k = 1
for i in range(4671032, 4671106 + 1):
    if f(i):
        print(k, i)
        k += 1