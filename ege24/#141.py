s = open('input.txt').read()
k = 0
i = 0
while i < len(s) - 2:
    if  s[i] == 'F' and s[i + 2] == 'O':
        k += 1
        i += 2
    else:
        i += 1
print(k)
