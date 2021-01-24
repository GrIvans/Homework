for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if (((x > 5) + (x * x <= a)) * ((y * y >= a) + (y <= 7))) == False:
                fl = False
    if fl:
        print(a)
#ans--25 (16)