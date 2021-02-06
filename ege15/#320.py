for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((2*y + 4*x != 100) or (a < 9*x) or (a < 3*y)) == False:
                fl = False
    if fl:
        print(a)
#ans--89 verno
