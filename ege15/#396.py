for a in range(1, 201):
    fl = True
    for x in range(1, 10001):
        if ((130 % a == 0) and (not(not(x % a == 0) and (x % 38 == 0)) or not (x % 78 == 0))) == False:
            fl = False
    if fl:
        print(a)
#ans--26 verno
