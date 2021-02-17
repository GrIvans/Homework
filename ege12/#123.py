s = '5' * 156
while s.find('333') != -1 or s.find('555') != -1:
    if s.find('555') != -1:
        s = s.replace('555', '3', 1)
    elif s.find('333') != -1:
        s = s.replace('333', '5', 1)
print(s)
#ans==53 verno
