for a in range(1, 201):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((3*y - 4*x - 29 != 0) or (a < 2*x**2 + 5) or (a < y**2 - 1)) == False:
                fl = False
    if fl:
        print(a)
#ans--119 verno
