for a in range(1, 1001):
    fl = True
    for x in range(1, 10001):
        if ((45 % a == 0) and (not((x % 30 == 0) and (x % 12 == 0)) or (x % a == 0))) == False:
            fl = False
    if fl:
        print(a)
#ans--15 verno
