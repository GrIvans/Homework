for a in range(-10, 21):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((y + 3*x != 60) or (x > a) or (y > a)) == False:
                fl = False
    if fl:
        print(a)
#ans--14 verno
