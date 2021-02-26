for a in range(1, 201):
    fl = True
    for x in range(1, 10001):
        if ((120 % a == 0) and (not(not(x % a == 0) and (x % 36 == 0)) or not (x % 15 == 0))) == False:
            fl = False
    if fl:
        print(a)
#ans--60 verno
