for a in range(1, 201):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if (((y * y >= a) + (y < 12)) * ((x > 11) + (x * x < a))) == 0:
                fl = False
    if fl:
        print(a)
#ans--122 (101)