for a in range(1, 201):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if (((y >= -4*x + 12) and (y >= 4*x - 12)) == (y >= a * abs(x - 3))) == False:
                fl = False
    if fl:
        print(a)
#ans--4 verno
