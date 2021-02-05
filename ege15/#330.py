for a in range(1, 201):
    fl = True
    for x in range(1, 201):
        for y in range(1, 201):
            for z in range(1, 201):
                if ((80 != 5*y + 2*x + 4*z) or (a < 6*x) or (a < y) or (a < 3*z)) == False:
                    fl = False
                    break
    if fl:
        print(a)
#ans--11 verno
