p = range(2, 21)
q = range(15, 31)
fl = True
a = range(0, 16)
for x in range(1, 1001):
    if (((x in a) or not(x in p)) or (x in q)) == False:
        fl = False
print(fl)
#ans--1 verno
