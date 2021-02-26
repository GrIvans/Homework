s = '1' * 50 + '2' * 50 + '3' * 50
while s.find('13') != -1 or s.find('32') != -1 or s.find('12') != -1:
    if s.find('13') != -1:
        s = s.replace('13', '31', 1)
    if s.find('32') != -1:
        s = s.replace('32', '23', 1)
    if s.find('12') != -1:
        s = s.replace('12', '21', 1)
print(s[9], s[69], s[139])
#ans==231 verno
