s = open('24data/24.txt').read()

k = ''
mn = ''
for i in range(len(s) - 1):
    if s[i] > s[i + 1]: 
        k += s[i]
    else:
        if len(mn) < len(k + s[i]):
            mn = k + s[i]
        k = ''
print(mn)
