s = open('input.txt').read()
s += 'A'
k = ''
mx = ''
for i in range(len(s) - 1):
    if s[i] < s[i + 1]: 
        k += s[i]
    else:
        k += s[i]
        if len(mx) < len(k):
            mx = k
        k = ''
print(mx)
