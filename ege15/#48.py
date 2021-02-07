p = range(10, 21)
q = range(5, 16)
fl = True
a = range(15, 23)
for x in range(1, 1001):
    if ((not(x in p) or (x in q)) or (x in a)) == False:
        fl = False
print(fl)
#ans--3 verno
