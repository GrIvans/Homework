for x in range(1, 100):
    for n in range(5, 36):
        if x**2 - int('30', n) * x + int('240', n) == 0:
            print(n, x)
