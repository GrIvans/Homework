s = open('input.txt').read()
fout = open('output.txt', 'w')
fout.write('Input file contains:\n')
kolvo_simv = 0
words = 0
lines = 0
word = ''
for i in s:
    if i.isalpha():
        kolvo_simv += 1
        word += i
    elif i == '\n':
        lines += 1
        words += 1
        word = ''
    elif i == ' ' and word != '':
        words += 1
        word = ''

fout.write(str(kolvo_simv) + ' letters\n')
fout.write(str(words) + ' words\n')
fout.write(str(lines) + ' lines\n')