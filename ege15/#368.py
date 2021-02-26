for a in range(1, 501):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((x**2 - 10*x + 16 > 0) or (y**2 - 10*y + 21 > 0) or (x * y < 2 * a)) == False:
                fl = False
    if fl:
        print(a)
# ans--29 verno
