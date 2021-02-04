for a in range(1, 101):
    for b in range(1, 101):
        fl = True
        for x in range(1, 101):
            for y in range(1, 101):
                if ((y <= ((x - 4)**2 + 2 + abs((x - 2)**2 -16))) == ((y <= 2 * x**2 - 12*x + a) or (y <= -4*x + b))) == False:
                    fl = False
        if fl:
            print(a, b)
#ans--36 verno
