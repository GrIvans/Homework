for a in range(100, 201):
    fl = True
    for x in range(1, 324 * 36):
        if ((not((x % a == 0) and (x % 36 == 0)) or (x % 324 == 0)) and (a > 100)) == False:
            fl = False
    if fl:
        print(a)
#ans--162 verno
