for a in range(1, 201):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((y <= (4 + abs(x + 8) + abs (x - 8))) == ((y <= 2*x + 4) or (y <= a))) == False:
                fl = False
    if fl:
        print(a)
#ans--20 verno
