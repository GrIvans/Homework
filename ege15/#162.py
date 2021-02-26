for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        if ((x & 29 == 0) or ((x & 9 != 0) or (x & a != 0))) == False:
            fl = False
    if fl:
        print(a)
# ans--20 verno
