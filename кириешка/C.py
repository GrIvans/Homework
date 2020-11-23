s = open('input.txt', 'r', encoding='utf-8').read()
s = s[:-1]
ansv = s[::-1]
with open('output.txt', 'w', encoding='utf-8') as fin:
    fin.write(ansv)
