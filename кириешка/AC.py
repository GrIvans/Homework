s = open('input.txt', encoding='utf-8')
fout = open('output.txt', 'w')
votes = {}
y = s.readline()
while True:
    y = s.readline()
    if y != 'VOTES:\n':
        votes[y] = 0
    else:
        break
kol = 0
while True:
    y = s.readline()
    if y != '':
        votes[y] += 1
        kol += 1
    else:
        break
for i in votes:
    if votes[i] / kol >= 0.07:
        fout.write(i)