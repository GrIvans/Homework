for a in range(1, 1001):
    fl = True
    for x in range(1, 1001):
        if ((x & a == 0) or (x & 29 != 0 or x & 86 != 0)) == False:
            fl = False
    if fl:
        print(a)
# ans--95 verno
