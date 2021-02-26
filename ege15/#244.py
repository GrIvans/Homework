for a in range(150, 301):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if (((y * y >= a) or (y < 16)) and ((x > 13) or (x * x < a))) == False:
                fl = False
    if fl:
        print(a)
#ans--255 (256)
