for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((y - 40 < a) * (30 - y < a)) + (x * y > 20) == 0:
                fl = False
    if fl:
        print(a)
# ans--30 verno
