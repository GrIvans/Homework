def f(a):
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            return False
    return True

k = 1
for i in range(194441, 196500 + 1):
    if f(i) and i % 100 == 93:
        print(k, i)
        k += 1
