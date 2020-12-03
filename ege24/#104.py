s = open('24data/24-1.txt').read()
m = ''
mx = ''
n = 1
mn = 1
for i in range(len(s) - 1):
    if ord(s[i]) < ord(s[i + 1]):
        if m == '':
            n = i + 1
        m += s[i]
    else:
        m += s[i]
        if len(m) > len(mx):
            mx = m
            mn = n
        m = ''
        n = 1
print(mn)
