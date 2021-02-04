for a in range(1, 501):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((x - 20 < a) and (20 - x < a) or (x * y > 50)) == False:
                fl = False
    if fl:
        print(a)
#ans--31 verno