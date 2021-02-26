for a in range(1, 22):
    fl = True
    for x in range(1, 1205):
        if (21 % a == 0 and (x % 40 != 0 or x % 30 != 0 or x % a == 0)) == False:
            fl = False
            break
    if fl:
        print(a)
# ans--3 verno
