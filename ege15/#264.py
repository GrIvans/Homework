k = 0
for a in range(1, 301):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if (((x > a) + (x * x <= 169)) * ((y * y > 16) + (y <= a))) == 0:
                fl = False
    if fl:
        k += 1
        print(a)
print('kolvo--', k)
#ans--10 (12)
