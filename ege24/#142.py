s = open('24data/24-s1.txt').read()
k = 0
i = 0
while i < len(s) - 2:
    if  s[i] == 'A' and s[i + 2] == 'R':
        k += 1
        i += 2
    else:
        i += 1
print(k)
