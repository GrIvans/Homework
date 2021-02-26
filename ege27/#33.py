data = open('27data/33/27-33a.txt')
#data = open('27data/33/27-33b.txt')
#data = open('input.txt')
D = 4
s, dmin = 0, [10001] * D
n = int(data.readline())
for i in range(n):
    a, b, c = map(int, data.readline().split())
    a, b, c = max(a, b, c), a + b + c - \
        max(a, b, c) - min(a, b, c), min(a, b, c)
    s += a + b
    d = min(a - c, b - c)
    r = d % D
    if r > 0:
        newdmin = dmin[:]
        for k in range(1, D):
            r0 = (r + k) % D
            newdmin[r0] = min(d + dmin[k], dmin[r0])
        newdmin[r] = min(d, dmin[r])
        dmin = newdmin[:]
if s % D == 0:
    print(s)
else:
    print(s - dmin[s % D])
# 1==18380 verno
# 2==58701760 verno
