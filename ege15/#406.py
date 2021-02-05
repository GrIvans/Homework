for a in range(1, 2001):
    fl = True
    for x in range(1, 10001):
        if (not(not(x % 84 == 0) or not(x % 90 == 0)) or not(x % a == 0)) == False:
            fl = False
    if fl:
        print(a)
#ans--1260 verno
