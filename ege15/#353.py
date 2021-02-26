for a in range(1, 201):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if (not(x < 9) or (not(5*y < x) or (2*x*y <a))) == False:
                fl = False
    if fl:
        print(a)
#ans--17 verno
