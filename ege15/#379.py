for a in range(1, 201):
    fl = True
    for x in range(1, 1001):
        if ((not(not(x % a == 0) and (x % 180 == 0)) or (x % 130 == 0)) and (a < 100)) == False:
            fl = False
    if fl:
        print(a)
#ans--90 verno
