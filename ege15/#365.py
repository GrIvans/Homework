for a in range(1, 501):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((x > 7) or (y > 4) or (x**2 + 3*y < a)) == False:
                fl = False
    if fl:
        print(a)
#ans--62 verno
