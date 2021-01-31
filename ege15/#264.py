k = 0
for a in range(1, 21):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if (((x >= a) or (x * x <= 169)) and ((y * y >= 16) or (y <= a))) == 0:
                fl = False
    if fl:
        k += 1
        print(a)
print('kolvo--', k)
#ans--12
