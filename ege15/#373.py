for a in range(1, 10000):
    fl = True
    for x in range(1, 2000):
        for y in range(1, 2000):
            if (((x - 30 < a) and (15 - y < a)) or (x * (y + 3) > 60)) == 0:
                fl = False
    if fl:
        print(a)
# ans--15 verno
