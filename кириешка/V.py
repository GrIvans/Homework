s = open('input.txt', encoding='utf-8').readlines()
fout = open('output.txt', 'w', encoding='utf-8')
ansv_dict = {}
for i in s:
    i = i.split()
    if int(i[3]) not in ansv_dict:
        ansv_dict[int(i[3])] = []
    ansv_dict[int(i[3])].append(i[0] + ' ' + i[1] + ' ' + i[3] + '\n')
for i in sorted(ansv_dict, reverse=True):
    for n in sorted(ansv_dict[i]):
        fout.write(n)
