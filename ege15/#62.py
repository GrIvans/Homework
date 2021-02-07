p = range(5, 11)
q = range(15, 21)
r = range(25, 31)
fl = True
a = range(5 , 11)
for x in range(1, 1001):
    if ((not(x in a) or (x in p)) == (not(x in q) or not(x in r))) == False:
        fl = False
print(fl)
#ans--1 verno
