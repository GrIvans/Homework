s = open('input.txt').read()
k = 0
n = s[0]
for i in range(1, len(s)):
    if s[i] > s[i - 1]:
        n += s[i]
    else:
        if len(n) == 5:
            k += 1
        n = ''
print(k)
