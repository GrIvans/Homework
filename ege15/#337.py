for a in range(1, 201):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((2*y + x != 17) or (a > 7*x) and (a > 3*y)) == False:
                fl = False
    if fl:
        print(a)
#ans--106 verno
