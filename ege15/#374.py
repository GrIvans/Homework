for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if (((x - 20 < a) and (10 - y < a)) or ((x + 4) * y > 45)) == False:
                fl = False
    if fl:
        print(a)
#ans--22 verno
