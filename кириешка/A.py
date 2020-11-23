s = open('input.txt', 'r', encoding='utf-8').read().split()
ansv = []
for i in s:
    ansv.append(int(i))
with open('output.txt', 'w', encoding='utf-8') as fin:
    fin.write(str(sum(ansv)))
