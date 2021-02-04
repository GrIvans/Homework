for a in range(1, 501):
    fl = True
    for x in range(1, 1001):
        if (not((x % 12 == 0) or (x % 36 == 0)) or (x % a == 0) and (a**2 - a - 90 < 0)) == False:
           fl = False
    if fl:
        print(a)
#ans--6 verno
