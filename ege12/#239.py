s = '>' + '1' * 20 + '2' * 15 + '3' * 40
while s.find('>1') != -1 or s.find('>2') != -1 or s.find('>3') != -1:
    if s.find('>1') != -1:
        s = s.replace('>1', '22>', 1)
    if s.find('>2') != -1:
        s = s.replace('>2', '2>1', 1)
    if s.find('>3') != -1:
        s = s.replace('>3', '1>2', 1)
print(sum(map(int, s[:-1])))
#ans==450 verno
