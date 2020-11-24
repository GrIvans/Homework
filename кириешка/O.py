s = open('input.txt', encoding='utf-8').readlines()
fout = open('output.txt', 'w', encoding='utf-8')
ansv_dict = {}
for i in s:
    i = i.split()
    number = int(i[3])
    if number not in ansv_dict:
        ansv_dict[number] = []
    name = str(i[0] + ' ' + i[1])
    ansv_dict[number].append(name)
result = sorted(ansv_dict, reverse=1)
if len(ansv_dict[result[0]]) == 1:
    fout.write(*ansv_dict[result[0]])
else:
    fout.write(str(len(ansv_dict[result[0]])))
