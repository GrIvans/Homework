for a in range(1, 115):
    fl = True
    for x in range(201):
        for y in range(201):
            for z in range(201):
                if ((48 != y + 2*x + z) or (a < x) or (a < y) or (a < z)) == False:
                    fl = False
    if fl:
        print(a)
#ans--11 verno
