for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if (((x >= 5) or (x * x <= a)) and ((y * y > a) or (y <= 7))) == False:
                fl = False
    if fl:
        print(a)
        break
#ans--16