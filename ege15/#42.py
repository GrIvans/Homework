p = range(5, 16)
q = range(12, 19)
fl = True
a = range(17, 24)
for x in range(1, 1001):
    if ((not(x in a) or (x in p)) or (x in q)) == False:
        fl = False
print(fl)
#ans--3 verno
