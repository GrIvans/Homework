for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((y + 2 * x != 77) or (a < 5 * x) or (a < y)) == False:
                fl = False
    if fl:
        print(a)
#ans--54 verno