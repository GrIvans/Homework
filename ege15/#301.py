for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((5*y - x > a) or (2*x + 3*y < 90) or (y - 2*x < -50)) == False:
                fl = False
    if fl:
        print(a)
#ans--19 verno
