for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((y - 2*x + 29 != 0) or (a < x) or (a < 3*y)) == False:
                fl = False
    if fl:
        print(a)
#ans--14 verno
