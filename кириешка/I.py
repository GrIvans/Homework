s = open('input.txt').read()
fout = open('output.txt', 'w')
ansver = 0
sm = ''
for i in s:
    if i.isdigit():
        sm += i
    else:
        if sm != '':
            ansver += int(sm)
        sm = ''
fout.write(str(ansver))
fout.close()