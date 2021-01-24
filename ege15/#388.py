for a in range(1, 1001):
    fl = True
    for x in range(1, 1001):
        if (120 % a == 0 and (x % 70 != 0 or x % 30 != 0) or x % a == 0) == False: 
            fl = False
    if fl:
        print(a)
