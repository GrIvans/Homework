for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((5*y + 3*x != 54) or (a < 2*x + 3) or (a < 4*y - 5)) == False:
                fl = False
    if fl:
        print(a)
#ans--18 verno
