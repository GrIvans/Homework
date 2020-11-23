fin = open('input.txt', 'r', encoding='utf-8').read()
fout = open('output.txt', 'w', encoding='utf-8')
fout.write(str(''.join(reversed(fin)) + '\n'))
fout.close()


