s = open('24data/k7-m4.txt').read()
s += 'A'
a = []
k = 0
for i in s:
    if i == 'C':
        k += 1
    else:
        if k != 0 and k > 5: a.append((k, (k - 1) * 'c' + 'C'))
        k = 0
num = 1
print(a)
for n in reversed(a):
    print(num, n[0], n[1])
    num += 1