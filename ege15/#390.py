for a in range(1, 301):
    fl = True
    for x in range(1, 10001):
        if ((110 % a == 0) and (not((x % 80 == 0) and (x % 75 == 0)) or (x % a == 0))) == False:
            fl = False
    if fl:
        print(a)
#ans--10 verno
