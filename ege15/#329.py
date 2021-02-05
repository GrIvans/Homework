for a in range(1, 201):
    fl = True
    for x in range(1, 201):
        for y in range(1, 201):
            for z in range(1, 201):
                if ((x + 3*y + 2*z - 54 != 0) or (a < x + 10) or (a < 5*y - 4*x) or (a < z + x)) == False:
                    fl = False
                    break
    if fl:
        print(a)
#ans--16 verno
