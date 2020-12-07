s = open('24data/24-s1.txt').read()
k = 0
i = 0
for i in range(len(s) - 3):
    if s[i] == 'Z' and s[i + 2] == 'R' and s[i + 3] == 'O':
        k += 1
print(k)
