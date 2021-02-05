for a in range(1, 201):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((3*y + x != 22) or (a > 5*x - 8) and (a > 2*y + 3)) == False:
                fl = False
    if fl:
        print(a)
#ans--88 verno
