s = open('24data/k7-m1.txt').read()
k = 0
ans = []
for i in s:
    if i == 'C':
        k += 1
    else:
        if k != 0:
            ans.append(k)
        k = 0
if k != 0:
    ans.append(k)
print(min(ans), len(ans), len(s))
