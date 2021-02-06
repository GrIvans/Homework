for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((y + 3*x != 60) or (2*x > a) or (y > a)) == False:
                fl = False
    if fl:
        print(a)
#ans--23 verno
