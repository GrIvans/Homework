for a in range(10, 201):
    fl = True
    for x in range(1, 1001):
        if ((not((x % a == 0) and (x % 375 == 0)) or (x % 100 == 0)) and (a > 10)) == False:
            fl = False
    if fl:
        print(a)
#ans--11 (12)
