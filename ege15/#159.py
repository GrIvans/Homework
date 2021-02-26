for a in range(1, 1001):
    fl = True
    for x in range(1, 1001):
        if ((x & a == 0) or (x & 14 != 0 or x & 75 != 0)) == False:
            fl = False
    if fl:
        print(a)
# ans--79 verno
