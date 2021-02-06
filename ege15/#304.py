for a in range(-100, 101):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((4*y - x > a) or (x + 6*y < 210) or (3*y - 2*x < 30)) == False:
                fl = False
    if fl:
        print(a)
#ans--89 verno
