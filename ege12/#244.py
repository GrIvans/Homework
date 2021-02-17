s = '1' * 50 + '2' * 50 + '3' * 50
while s.find('21') != -1 or s.find('31') != -1 or s.find('23') != -1:
    if s.find('21') != -1:
        s = s.replace('21', '12', 1)
    if s.find('31') != -1:
        s = s.replace('31', '13', 1)
    if s.find('23') != -1:
        s = s.replace('23', '32', 1)
print(s[9], s[89], s[129])
#ans==132 verno
