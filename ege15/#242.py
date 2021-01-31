for a in range(1, 501):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((x > 11) or (x * x <= a)) and ((y * y >= a) or (y <= 12)) == 0:
                fl = False
    if fl:
        print(a)
#ans--169
