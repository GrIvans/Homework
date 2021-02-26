for a in range(1, 1001):
    fl = True
    for x in range(1, 1001):
        if ((x & a == 0) or (x & 44 != 0 or x & 76 != 0)) == False:
            fl = False
    if fl:
        print(a)
# ans--108 verno
