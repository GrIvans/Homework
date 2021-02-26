for a in range(-100, 101):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((3*y - x > a) or (2*x + 3*y < 30) or (2*y - x < -31)) == False:
                fl = False
    if fl:
        print(a)
#ans-- -31 verno
