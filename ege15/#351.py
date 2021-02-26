for a in range(-50, 201):
    fl = True
    for k in range( 1001):
        for m in range( 1001):
            if ((k + m > 10) or ((k + m > a) and (k - m > a))) == False:
                fl = False
    if fl:
        print(a)
#ans-- -11 verno
