s = open('input.txt', 'r', encoding='utf-8').readlines()
ansvers = {}
for i in s:
    ss = i.split()
    if ss[2] not in ansvers:
        ansvers[ss[2]] = []
    ansvers[ss[2]].append(int(ss[3]))
mx9 = max(ansvers['9'])
mx10 = max(ansvers['10'])
mx11 = max(ansvers['11'])
print(ansvers)
kol9, kol10, kol11 =0, 0, 0
for i in ansvers['9']:
    if i == mx9:
        kol9 += 1
for i in ansvers['10']:
    if i == mx10:
        kol10 += 1
for i in ansvers['11']:
    if i == mx11:
        kol11 += 1
with open('output.txt', 'w', encoding='utf-8') as fout:
    fout.write(str(kol9) + ' ' + str(kol10) + ' ' + str(kol11))
