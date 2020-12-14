s = open('24data/24-j8.txt').read()
s = s[:-1]
s += '0'
mx_ln = 0
k = 0
ln = 2
for i in range(1, len(s) - 1):
    if int(s[i - 1]) + int(s[i]) >= 10 and int(s[i]) + int(s[i + 1]) >= 10:
        ln += 1
    else:
        mx_ln = max(mx_ln, ln)
        ln = 2
print(mx_ln)