for a in range(-100, 1001):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if (( y - x > a) or (x + 4*y > 40) or (y - 2*x < -35)) == False:
                fl = False
    if fl:
        print(a)
#ans-- -18 verno
