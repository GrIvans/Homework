for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((3*y - 9*x + 51 != 0) or ((a < 6*x) or (a < 3*y))) == False:
                fl = False
    if fl:
        print(a)
#ans--35 verno
