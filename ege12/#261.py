s = 'AB' * 52
while s.find('AA') != -1 or s.find('BB') != -1 or s.find('AB') != -1:
    s = s.replace('AA', 'B', 1)
    s = s.replace('BB', 'A', 1)
    s = s.replace('AB', 'BA', 1)
print(s)
#ans==BA verno
