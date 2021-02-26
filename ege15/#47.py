p = range(10, 21)
q = range(12, 16)
fl = True
a = range(5, 21)
for x in range(1, 1001):
    if (((x in a) or not(x in p)) or (x in q)) == False:
        fl = False
print(fl)
#ans--3 verno
