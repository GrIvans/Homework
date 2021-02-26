for a in range(1, 501):
    fl = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if (((y - 20 < a) and (10 - x < a)) or (x * (y + 2) > 48)) == 0:
                fl = False
    if fl:
        print(a)
# ans--27 verno
