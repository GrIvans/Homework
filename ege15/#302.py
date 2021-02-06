for a in range(100, 1001):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((5*y + 4*x > a) or (2*x + 3*y < 92) or (y - 2*x < -150)) == False:
                fl = False
    if fl:
        print(a)
#ans--153 verno
