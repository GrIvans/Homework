for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((y - x + 10 != 0) or (a < 3*x) or (a < y)) == False:
                fl = False
    if fl:
        print(a)
#ans--32 verno
