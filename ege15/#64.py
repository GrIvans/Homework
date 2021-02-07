p = range(10, 31)
q = range(15, 31)
r = range(25, 36)
fl = True
a = range(5, 21)
for x in range(1, 1001):
    if (((x in a) or not(x in p)) == (not(x in q) or not(x in r))) == False:
        fl = False
print(fl)
#ans--4
