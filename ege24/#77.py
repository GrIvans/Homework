s = open('24data/k8-1.txt').read()

mx = 0
k = 0

for i in range (1, len(s) - 1):
    if s[i - 1] != s[i + 1] != s[i]:
        k += 1
    else:
        mx = max(k, mx)
        k = 0
print(mx)
