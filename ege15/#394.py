for a in range(1, 201):
    fl = True
    for x in range(1, 1001):
        if ((40 % a == 0) and (not(not(x % a == 0) and (x % 54 == 0)) or not (x % 72 == 0))) == False:
            fl = False
    if fl:
        print(a)
#ans--8 verno
