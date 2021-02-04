for a in range(1, 1001):
    fl = True
    for x in range(1, 1001):
        if ((not((x & 13 != 0) or (x & a != 0)) or (x & 13 != 0)) or ((x & a != 0) and (x & 39 == 0))) == False:
            fl = False
    if fl:
        print(a)
# ans--13 verno
