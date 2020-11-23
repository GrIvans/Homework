s = open('input.txt', encoding='utf-8').readlines()
ansvers = {}
for i in s:
    ss = i.split()
    if ss[2] not in ansvers:
        ansvers[ss[2]] = []
    ansvers[ss[2]].append(int(ss[3]))
print((str(max(ansvers['9'])) + ' ' + str(max(ansvers['10'])) + ' ' +str(max(ansvers['11']))))
