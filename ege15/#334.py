for a in range(399, 1001):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((17*y - 13*x != 480) or (a < (x + 5)**2) or (a < 19*y)) == False:
                fl = False
    if fl:
        print(a)
#ans--550 verno
