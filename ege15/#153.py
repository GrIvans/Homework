for a in range(1000):
    fl = True
    for x in range(1000):
        if ((x & 102 == 0) + (x & 36 != 0) + (x & a != 0)) == 0:
            fl = False
    if fl:
        print(a)
# ans--66 verno
