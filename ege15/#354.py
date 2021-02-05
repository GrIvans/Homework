k = 0
for a in range(1, 50):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((2*x + 3*y != 13) or (2*y + 3*x != 12) or ((x**2 + 3*x - 1 < a) and (2*y**2 - 4*y + 20 > a))) == False:
                fl = False
    if fl:
        print(a)
        k += 1
print(k)
#ans--16 verno
