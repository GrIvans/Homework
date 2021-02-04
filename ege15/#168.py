for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        if (not((x & 28 != 0) or (x & 45 != 0)) or (not(x & 17 == 0) or (x & a != 0))) == False:
            fl = False
    if fl:
        print(a)
# ans--44 verno
