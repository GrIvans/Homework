for a in range(1, 201):
    fl = True
    for x in range(1001):
        for y in range(1001):
            if ((5*x - 6*y < a) or (x - y > 30)) == False:
                fl = False
    if fl:
        print(a)
#ans--151 verno
