for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((x >= 10) or (x < y) or (x * y < a)) == False:
                fl = False
    if fl:
        print(a)
        break
# ans--82 verno
