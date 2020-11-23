s = open('input.txt').read()
fout = open('output.txt', 'w')
if s.find('@') != -1:
    fout.write('YES')
else:
    fout.write('NO')
fout.close()