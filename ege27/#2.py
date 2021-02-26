data = open('27data/2/27-2a.txt')
#data = open('27data/2/27-2b.txt')
#data = open('input.txt')
D = 3
s = 0
dMin = [10001] * D
n = int(data.readline())
for i in range(n):
    a, b = map(int, data.readline().split())
    s += max(a, b)
    d = abs(a - b)
    r = d % D
    if r > 0:
        dMinNew = dMin[:]
        for k in range(1, D):
            r0 = (r + k) % D
            dMinNew[r0] = min(d + dMin[k], dMin[r0])
        dMinNew[r] = min(d, dMin[r])
        dMin = dMinNew[:]

if s % D == 0:
    print(s)
else:
    print(s - dMin[s % D])
# 1==109737 verno
# 2==401536407 verno
