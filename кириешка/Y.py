s = open('input.txt', encoding='utf-8').readlines()
out = 0
ansv_dict = {}
for x in s:
    i = x.split()
    if int(i[2]) not in ansv_dict:
        ansv_dict[int(i[2])] = []
    ansv_dict[int(i[2])].append(int(i[3]))
ansver = []
mx_sred = 0
for i in ansv_dict:
    kolvo = len(ansv_dict[i])
    summa = sum(ansv_dict[i])
    sred = summa / kolvo
    mx_sred = max(sred, mx_sred)
    ansv_dict[i] = sred
for i in sorted(ansv_dict, key=ansv_dict.get):
    if ansv_dict[i] == mx_sred:
        ansver.append(i)
for i in sorted(ansver):
    print(i, end=' ')
