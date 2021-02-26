k = 0
for a in range(1, 201):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((-5*x + y != -7) or (x**2 - y != 1) or ((x + 3*y > a) and (y - x <= a))) == False:
                fl = False
    if fl:
        print(a)
        k += 1
print(k)
#ans--6 verno
