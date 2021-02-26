for a in range(1, 501):
    fl = True
    for x in range(1, 1001):
        if ((x % a == 0) and (a < 10) or not(x % 44 == 0) and not(x % 99 == 0) and (a < 10)) == False:
            fl = False
    if fl:
        print(a)
#ans--1 verno
