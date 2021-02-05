for a in range(1, 201):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((2*y + 5*x != 17) or (a > 2*x + 3*y) and (a > 4*y + x + 1)) == False:
                fl = False
    if fl:
        print(a)
#ans--27 verno
