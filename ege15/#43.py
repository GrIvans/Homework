p = range(5, 11)
q = range(15, 19)
fl = True
a = range(6, 11)
for x in range(1, 1001):
    if ((not(x in a) or (x in p)) or (x in q)) == False:
        fl = False
print(fl)
#ans--2 verno
