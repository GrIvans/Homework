for a in range(1, 201):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((x - 2*y < 3*a) or (2*y > x) or (3*x > 50)) == False:
                fl = False
    if fl:
        print(a)
#ans--5 verno
