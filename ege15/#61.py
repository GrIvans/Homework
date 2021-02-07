p = range(10, 16)
q = range(10, 21)
r = range(5, 16)
fl = True
a = range(12, 21)
for x in range(1, 1001):
    if ((not(x in a) or (x in p)) == (not(x in q) or (x in r))) == False:
        fl = False
print(fl)
#ans--3 verno
