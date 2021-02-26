for a in range(1, 501):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if (((y * y > a) or (y <= 15)) and ((x > 3) or (x * x < a))) == False:
                fl = False
    if fl:
        print(a)
#ans--256 (255)
