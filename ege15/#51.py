p = range(0, 21)
q = range(5, 16)
r = range(35, 51)
fl = True
a = range(-15, -4)
for x in range(1, 1001):
    if ((not(x in p) or (x in q)) or (not(x in a) or (x in r))) == False:
        fl = False
print(fl)
#ans--1 verno
