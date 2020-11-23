s = open('input.txt')
fout = open('output.txt', 'w')
for i in s:
    sm = 0
    ss = i.split()
    for now in ss:
        sm += int(now)
    fout.write(str(sm) + '\n')