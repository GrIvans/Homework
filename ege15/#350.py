for a in range(-20,  1001):
    fl = True
    for k in range(1001):
        for m in range(1001):
            if ((k + m > 12) or ((k - 10 > a) and (m + 10 > a))) == False:
                fl = False
    if fl:
        print(a)
#ans-- -11 verno
