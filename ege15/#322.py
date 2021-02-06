for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((y + 7*x != 498) or (a < x + 18) or (a < 6*y - 3)) == False:
                fl = False
    if fl:
        print(a)
#ans--86 verno
