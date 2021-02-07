p = range(20, 51)
q = range(15, 21)
r = range(40, 81)
fl = True
a = range(40, 51)
for x in range(1, 1001):
    if (((not(x in p) or (x in q)) or (not(x in a) or (x in r)))) == False:
        fl = False
print(fl)
#ans--3 verno
