for a in range(1, 1001):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if (not(x <= 5) or (x * x <= a)) and (not(y * y <= a) or y < 7) == 0:
                fl = False
    if fl:
        print(a)
# ans--48 верно
