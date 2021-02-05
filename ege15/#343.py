for a in range(1, 201):
    fl = True
    for x in range( 1001):
        for y in range( 1001):
            if ((50 > x) and (144 >= 4*y - 3*x) and (a**2 < (x-25)**2 + (y - 25)**2)) == False:
                fl = False
    if fl:
        print(a)
#ans--
