s = '8' * 146
while s.find('222') != -1 or s.find('888') != -1:
    if s.find('222') != -1:
        s = s.replace('222', '8', 1)
    if s.find('888') != -1:
        s = s.replace('888', '2', 1)
print(s)
#ans==88 verno
