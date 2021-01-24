for a in range(1, 1001):
    fl = True
    for x in range(1, 1001):
        if ((x & 25 == 0) or (x & 17 != 0 or x & a != 0)) == False:
            fl = False
    if fl:
        print(a)
# ans--8 verno
