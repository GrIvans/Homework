for a in range(1, 1001):
    fl = True
    for x in range(1, 10001):
        if ((33 % a == 0) and (not((x % 56 == 0) and (x % 20 == 0)) or (x % a == 0))) == False:
            fl = False
    if fl:
        print(a)
#ans--1 verno
