s = open('24data/24-j6.txt').read()
s += '0'
k = 0
n = s[0]
for i in range(1, len(s)):
    if (s[i]) > (s[i - 1]):
        n += s[i]
    else:
        if len(n) == 5:
            k += 1
        n = s[i]
print(k)
