s = '1' * 198
while s.find('1111') != -1:
    s = s.replace('1111', '33', 1)
    s = s.replace('333', '1', 1)
print(s)
#ans==13 verno
