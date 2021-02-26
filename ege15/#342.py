for a in range(1, 801):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((x > 40) or (5*y - 3*x > 150) or (a >= (x - 20)**2 + (y - 20)**2)) == False:
                fl = False
    if fl:
        print(a)
#ans--
