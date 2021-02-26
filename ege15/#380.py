for a in range(1, 201):
    fl = True
    for x in range(1, 1001):
        if ((not((x % 36 == 0) and (x % 42 == 0)) or (x % a == 0)) and (a*(a - 25) < 25 * (a + 200))) == False:
            fl = False
    if fl:
        print(a)
#ans--84 verno
