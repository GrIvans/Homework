for a in range(1, 501):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((x > 4) or (x + 2 < y) or (x**2 + y**2 < a)) == False:
                fl = False
    if fl:
        print(a)
#ans--53 verno
