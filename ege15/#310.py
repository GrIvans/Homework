for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((4*y + 3*x != 65) or (x > a) or (3*y > a)) == False:
                fl = False
    if fl:
        print(a)
#ans--14 verno
