for a in range(50, 121):
    fl = True
    for x in range(1, 10001):
        if not(x & a == 0) or (not(x & 31 != 0) or x & 35 != 0) == 0:
            fl = False
    if fl:
        print(a)
