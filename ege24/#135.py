s = open('24data/24-j4.txt').read()
s += ' '
k = 0
for i in range(1, len(s) - 4):
    if s[i] == 'B' and s[i + 1] == 'O' and s[i + 2] == 'S' and s[i + 3] == 'S' and\
        s[i - 1] != 'J' and s[i + 4] != 'J':
        k += 1
print(k)
