p = range(15, 31)
q = range(0, 11)
r = range(25, 36)
fl = True
a = range(35, 41)
for x in range(1, 1001):
    if (((not(x in p) or (x in q)) or (not(x in a) or (x in r)))) == False:
        fl = False
print(fl)
#ans--4 verno
