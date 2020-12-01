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
print(ansv)
