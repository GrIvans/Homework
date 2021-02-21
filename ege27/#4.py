data = open('27data/4/27-4a.txt')
data = open('27data/4/27-4b.txt')
#data = open('input.txt')
D = 5
n = int(data.readline())
s, dMin = 0, [10001] * D
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
    print(s - dMin[(s % D)])
# 1==123720 verno
# 2==402332230 verno
