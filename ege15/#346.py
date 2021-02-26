for a in range(1, 10):
    fl = True
    for k in range(1,  1001):
        for n in range(1,  1001):
            if ((7*k + 2*n > 17) or ((k < a) and (n <= a))) == False:
                fl = False
    if fl:
        print(a)
#ans--5 verno
