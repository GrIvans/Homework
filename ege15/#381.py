for a in range(1000, 1111):
    fl = True
    for x in range(1, 2001):
        if ((not(x % a == 0) or (x % 36 == 0) and (x % 126 == 0)) and (a > 1000)) == False:
            fl = False
    if fl:
        print(a)
#ans--1008 verno
