s = open('24data/k8-0.txt').read()
ans = []
k = 0
mx_k = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        k += 1
    else:
        ans.append((k + 1, s[i]))
        mx_k = max(mx_k, k + 1)
        k = 0

for i in ans:
    if i[0] == mx_k:
        print(i[1], i[0])
