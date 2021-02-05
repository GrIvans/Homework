for a in range(1, 201):
    fl = True
    for x in range(2001):
        for y in range(0, 2001):
            if ((5*x + 3*y != 60) or ((a > x) and (a > y))) == False:
                fl = False
    if fl:
        print(a)
#ans--21 verno
