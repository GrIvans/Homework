for a in range(1, 201):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if (((y * y > a) or (y < 12)) and ((x >= 11) or (x * x < a))) == 0:
                fl = False
    if fl:
        print(a)
#ans--101