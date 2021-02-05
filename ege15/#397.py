for a in range(1, 201):
    fl = True
    for x in range(1, 10001):
        if ((108 % a == 0) and (not(not(x % a == 0) and (x % 42 == 0)) or not (x % 68 == 0))) == False:
            fl = False
    if fl:
        print(a)
#ans--12 verno
