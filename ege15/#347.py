for a in range(1, 201):
    fl = True
    for t in range(1, 1001):
        for m in range(1, 1001):
            if ((3*t + 8*m > 89) or ((m < a) and (t <= a))) == False:
                fl = False
    if fl:
        print(a)
#ans--27 verno
