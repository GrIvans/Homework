s = '1' * 170 + '3' * 100 + '2' * 7
while s.find('11') != -1:
    s = s.replace('112', '4', 1)
    s = s.replace('113', '2', 1)
    s = s.replace('42', '3', 1)
    s = s.replace('43', '1', 1)
print(s)
#ans==22 verno
