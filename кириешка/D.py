s = open('input.txt', 'r', encoding='utf-8').readlines()
fout = open('output.txt', 'w', encoding='utf-8')
for i in reversed(s):
    fout.write(i)
fout.close()
