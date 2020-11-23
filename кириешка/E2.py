s = open('input.txt').readlines()
a = []
for i in reversed(s):
    line = ''
    for j in reversed(i):
        line += j
    a.append(line)
    line = ''
with open('output.txt', 'w') as f:
    f.write('\n')
    f.writelines(a)
    f.write('\n')