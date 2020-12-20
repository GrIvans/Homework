fin = open('26data/26-k6.txt')
n, k = map(int, fin.readline().split())
a = []

for i in range(n):
    s, v = map(int, fin.readline().split())
    a.append((s, v))

a = sorted(a, key=lambda x: (x[1] / x[0], -x[1]))
s = 0
for i in range(k):
    s += a[i][0]
print(s, a[0][1])