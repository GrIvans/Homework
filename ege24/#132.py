s = open('24data/24-J1.txt').read()

k = 0
mx = 0
#не работает
for i in range(len(s) - 2):
    if s[i] == 'K' and\
        s[i + 1] == 'O' and\
        s[i + 2] == 'T':
        k += 1
    else:
        mx = max(mx, k)
print(k)
