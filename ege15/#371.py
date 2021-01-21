for a in range(1, 10001):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((y - 40 < a) and (30 - y < a)) or (x * y > 20) == 0:
                fl = False
    if fl:
        print(a)
#не работает