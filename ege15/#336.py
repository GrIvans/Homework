for a in range(1, 1001):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((y - x**2 != 80) or (a < 13*x - 14) or (a < y**2 + 15)) == False:
                fl = False
    if fl:
        print(a)
#ans--
