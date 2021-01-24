for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((y * y >= a or y <= 10) and (x >= 9 or x * x < a)) == False:
                fl = False
    if fl:
        print(a)
#ans--65 (82)
