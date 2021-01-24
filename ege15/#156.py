for a in range(1, 1001):
    fl = True
    for x in range(1, 1001):
        if ((x & a == 0) or (x & 30 != 0 or x % 20 != 0)) == False:
            fl = False
            break
    if fl:
        print(a)
#ans--31 (30)