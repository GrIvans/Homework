for a in range(1, 501):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((y * y >= a) + (y <= 15)) * ((x >= 3) + (x * x < a)) == 0:
                fl = False
    if fl:
        print(a)
#ans--256 (255)