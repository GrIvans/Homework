for a in range(1, 201):
    fl = True
    for k in range(1, 1001):
        for m in range(1, 1001):
            if ((5*k + 9*m > 121) or ((k - 13 <= a) and (m + 12 < a))) == False:
                fl = False
    if fl:
        print(a)
#ans--25 verno
