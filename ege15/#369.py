for a in range(1, 501):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((x**2 - 11*x + 28 > 0) or (y**2 - 9*y + 14 > 0) or (x**2 + y**2 > a)) == False:
                fl = False
    if fl:
        print(a)
# ans--19 verno
