s = '>' + '1' * 25 + '2' * 17 + '3' * 10
while s.find('>1') != -1 or s.find('>2') != -1 or s.find('>3') != -1:
    if s.find('>1') != -1:
        s = s.replace('>1', '22>3', 1)
    if s.find('>2') != -1:
        s = s.replace('>2', '2>', 1)
    if s.find('>3') != -1:
        s = s.replace('>3', '11>2', 1)
print(sum(map(int, s[:-1])))
#ans==274 verno
