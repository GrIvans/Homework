for a in range(1, 201):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((2*y + 3*x != 23) or (a > 2*x + 3) and (a > 3*y + 11)) == False:
                fl = False
    if fl:
        print(a)
#ans--42 verno
