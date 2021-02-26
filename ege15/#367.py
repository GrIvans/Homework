for a in range(1, 501):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((x**2 - 3*x + 2 > 0) or (y > x**2 + 7) or (x*y < a)) == False:
                fl = False
    if fl:
        print(a)
# ans--23 verno
