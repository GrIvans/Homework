p = range(25, 31)
q = range(15, 21)
fl = True
a = range(26, 29)
for x in range(1, 1001):
    if ((not(x in a) or (x in p)) or (x in q)) == False:
        fl = False
print(fl)
#ans--4 verno
