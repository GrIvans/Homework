for a in range(1, 201):
    fl = True
    for x in range(1, 201):
        for y in range(1, 201):
            for z in range(1, 201):
                if ((156 != 4*y + x**2 + 3*z) or (a < 8*x**2) or (a <y) or (a < 4*z)) == False:
                    fl = False
                    break
    if fl:
        print(a)
#ans--31 verno
