p = range(10, 26)
q = range(0, 13)
fl = True
a = range(12, 41)
for x in range(1, 1001):
    if (((x in a) or not(x in p)) or (x in q)) == False:
        fl = False
print(fl)
#ans--4 verno
