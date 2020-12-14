s = open('24data/k7-m2.txt').read()
s += 'A'
a = []
k = 0
for i in s:
    if i == 'C':
        k += 1
    else:
        if k != 0: a.append(k)
        k = 0
print(max(a), len(a), len(s) - 1)
