p = range(10, 21)
q = range(15, 26)
fl = True
a = range(8, 18)
for x in range(1, 1001):
    if ((not(x in p) or (x in q)) or (x in a)) == False:
        fl = False
print(fl)
#ans--1 verno
