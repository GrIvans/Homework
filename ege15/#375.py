for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((x * y > a) and (x > y) and (x < 8)) != False:
                fl = False
    if fl:
        print(a)
#ans--42 verno