s = open('input.txt', encoding='utf-8').readlines()
fout = open('output.txt', 'w', encoding='utf-8')
ansv = []
for i in s:
    i = i.split()
    ansv.append(i[0] + ' ' + i[1] + ' ' + i[3] + '\n')
ansv.sort()
for i in ansv:
    fout.write(i)