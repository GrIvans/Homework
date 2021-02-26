for a in range(200, 400):
    fl = True
    for x in range(1, 100000):
        if ((not((x % a == 0) and (x % 45 == 0)) or (x % 162 == 0)) and (a > 200)) == False:
            fl = False
    if fl:
        print(a)
#ans--324 verno
