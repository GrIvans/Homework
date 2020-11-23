fin = open('input.txt')
file = open('output.txt', 'w')
k_le, k_w, k_l = 0, 0, 0
word = ''
for x in fin.read():
    if x.isalpha():
        k_le += 1
        word += x
    elif word != '':
        k_w += 1
        word = ''
    if x == '\n':
        k_l += 1
        
file = open('output.txt', 'w', encoding='utf-8')
file.write('Input file contains:' + '\n')
file.write(str(k_le) + ' ' + 'letters' + '\n')
file.write(str(k_w) + ' ' + 'words' + '\n')
file.write(str(k_l) + ' ' + 'lines' + '\n')
file.close()
