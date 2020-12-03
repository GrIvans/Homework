s = open('24data/k7-m3.txt').read()
ansv = []
len_s = 0
for i in s: 
    if i == 'C':
        len_s += 1
    else:
        if 0 < len_s < 5: 
            ansv.append(len_s)
        len_s = 0
if len_s != 0:
    ansv.append(len_s)
num = 1
for i in ansv:
    st = (i * 'c').title()
    print(num, i, st)
    num += 1    
