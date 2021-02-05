for a in range(22, 1001):
    fl = True
    for x in range(1, 1001):
        if (not((x % (a - 21) == 0) and (x % (40 - a) == 0)) or (x % 90 == 0)) == False:
            fl = False
    if fl:
        print(a)
#ans--30 verno
