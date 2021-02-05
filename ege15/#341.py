for a in range(1, 201):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((6*x + 4*y != 34) or (a > 5*x + 3*y) and (a > 4*y + 15*x - 35)) == False:
                fl = False
    if fl:
        print(a)
#ans--45 verno
