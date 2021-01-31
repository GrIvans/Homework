for a in range(1, 1001):
    fl = True
    for x in range(1, 201):
        for y in range(1, 201):
            for z in range(1, 201):
                if ((220 != y + 2 * x + z) or (a < 6 * x) or (a < y) or (a < 2 * z)) == False:
                    fl = False
                    break
    if fl:
        print(a)
# ans--119 verno
