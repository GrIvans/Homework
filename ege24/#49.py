s = open('24data/k7-m24.txt').read()
s += '{'
k = 0

for i in range(len(s) - 2):
    if s[i] >= s[i + 1] >= s[i + 2]:
        k += 1
        num = i
print(k, num)
