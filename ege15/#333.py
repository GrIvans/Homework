for a in range(1, 201):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((21*y - 5*x != -99) or (a < 2*x - 7) or (a < y**2 +16)) == False:
                fl = False
    if fl:
        print(a)
#ans--40 verno
