s = '1' * 50 + '2' * 50 + '3' * 50
while s.find('12') != -1 or s.find('32') != -1 or s.find('31') != -1:
    if s.find('12') != -1:
        s = s.replace('12', '21', 1)
    if s.find('32') != -1:
        s = s.replace('32', '23', 1)
    if s.find('31') != -1:
        s = s.replace('31', '13', 1)
print(s[19], s[79], s[119])
#ans==213 verno
