s = open('24data/24-5.txt').read()
k = 0
for i in range(len(s) - 1):
    if s[i] == '(' and s[i + 1] == ')':
        k += 1
print(k)