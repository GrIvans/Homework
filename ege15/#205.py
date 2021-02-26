for a in range(50, 121):
    fl = True
    for x in range(1, 10001):
        if (x & a != 0) + ((x & 31 == 0) + x & 35 != 0) == 0:
            fl = False
    if fl:
        print(a)
# ans--95 verno
