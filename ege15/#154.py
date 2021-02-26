for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        if (x & 94 == 0) + ((x & 21 != 0) + (x & a != 0)) == 0:
            fl = False
    if fl:
        print(a)
# ans--74 verno
