s = open('input.txt', 'r', encoding='utf-8').read().split()
ansv = 0
for i in s:
    ansv += int(i)
with open('output.txt', 'w', encoding='utf-8') as fin:
    fin.write(str(ansv))
