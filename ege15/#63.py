p = range(10, 26)
q = range(15, 31)
r = range(25, 36)
fl = True
a = range(5, 16)
for x in range(1, 1001):
    if (((x in a) or not(x in p)) == (not(x in q) or (x in r))) == False:
        fl = False
print(fl)
#ans--3 
