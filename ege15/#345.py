for a in range(1, 201):
    fl = True
    for x in range( 1001):
        for y in range( 1001):
            if ((2*x + 3*y != 72) or ((a > x) and (a > y))) == False:
                fl = False
    if fl:
        print(a)
#ans--37 verno
