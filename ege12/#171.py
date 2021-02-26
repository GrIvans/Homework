s = '5' + '6' * 152 + '5'
while s.find('63') != -1 or s.find('664') != -1 or s.find('6665') != -1:
    if s.find('63') != -1:
        s = s.replace('63', '4', 1)
    if s.find('664') != -1:
        s = s.replace('664', '65', 1)
    if s.find('6665') != -1:
        s = s.replace('6665', '663', 1)
print(s)
#ans==5665
