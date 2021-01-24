for a in range(1, 301):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((y * y > a) + (y < 16)) * ((x >= 13) + (x * x < a)) == 0:
                fl = False
    if fl:
        print(a)
#ans--255 (256)
