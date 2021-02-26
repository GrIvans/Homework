for a in range(60, 201):
    fl = True
    for x in range(1, 1001):
        if ((not(x % a == 0) or (x % 54 == 0) or (x % 130 == 0)) and (a > 60)) == False:
            fl = False
    if fl:
        print(a)
#ans--108 verno
