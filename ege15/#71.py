p = range(30, 46)
q = range(40, 56)
fl = True
a = range(25, 66)
for x in range(1, 1001):
    if (((x in a)) or not(x in p)) == False or \
        (not (x in q) or (x in a)) == False:
        fl = False
print(fl)
#ans--2 verno
