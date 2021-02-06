for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((y + 5*x != 80) or (3*x > a) or (y > a)) == False:
                fl = False
    if fl:
        print(a)
#ans--29 verno
