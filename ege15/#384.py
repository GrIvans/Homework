for a in range(1, 21):
    fl = True
    for x in range(1, 375 * 100 + 1):
        if ((not((x % a == 0) and (x % 375 == 0)) or (x % 100 == 0)) and (a > 10)) == False:
            fl = False
    if fl:
        print(a)
#ans--12 verno
