s = '3' + '5' * 57
while s.find('25') != -1 or s.find('355') != -1 or s.find('4555') != -1:
    if s.find('25') != -1:
        s = s.replace('25', '3', 1)
    if s.find('355') != -1:
        s = s.replace('355', '4', 1)
    if s.find('4555') != -1:
        s = s.replace('4555', '2', 1)
print(s)
#ans==45 verno
