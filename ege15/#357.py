for a in range(1, 201):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if (((y <= 5*x - 14) and (y <= -5*x + a)) == (y - 6 <= -5 * abs(x - 4))) == False:
                fl = False
    if fl:
        print(a)
#ans--26 verno
