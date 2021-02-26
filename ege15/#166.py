for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        if ((not((x & 13 != 0) or (x & a == 0)) or (x & 13 != 0)) or ((x & a != 0) or (x & 39 == 0))) == False:
            fl = False
    if fl:
        print(a)
# ans--34 verno
