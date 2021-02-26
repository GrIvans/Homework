for a in range(1, 1001):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if (not(5*y + 2*x == 65) or (not(2*x <= a) or (3*y > a))) == False:
                fl = False
    if fl:
        print(a)
#ans--26 verno
