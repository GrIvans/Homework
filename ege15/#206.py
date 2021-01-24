k = 0
for a in range(1, 101):
    fl = True
    for x in range(1, 1001):
        if (x & 7 != 0 + x & 54 == 0 + x & a != 0 + (x & 27 == 0 * x & a != 0 * x & 7!= 0)) == 1:
            fl = False
    if fl:
        k += 1
print(k)
#ans--48