for a in range(1, 201):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((y <= abs(x**2 - 4*x - 5)) == ((y <= x**2 - 4*x - 5) or (y <= -(x - 2)**2 + a))) == False:
                fl = False
    if fl:
        print(a)
#ans--9 verno
