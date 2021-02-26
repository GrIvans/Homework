for a in range(1, 201):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((75 != 2*x + 3*y) or (a > 3*x) or(a > 2*y)) == False:
                fl = False
    if fl:
        print(a)
#ans--35 verno
