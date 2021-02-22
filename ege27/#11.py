data = open('27data/11/27-11a.txt')
#data = open('27data/11/27-11b.txt')
#data = open('input.txt')
# 1--14432 верно
# 2--45978688 верно
D = 8
n = int(data.readline())
s, dMin = 0, [10001] * D
for i in range(n):
    a, b, c = map(int, data.readline().split())
    a, b, c = max(a, b, c), a + b + c - max(a, b, c) - \
        min(a, b, c), min(a, b, c)
    s += a
    d = min(a - b, a - c)
    r = d % D
    if r > 0:
        dMinNew = dMin[:]
        for k in range(1, D):
            r0 = (r + k) % D
            dMinNew[r0] = min(d + dMinNew[k], dMin[r0])
        dMinNew[r] = min(d, dMin[r])
        dMin = dMinNew[:]
if s % D == 0:
    print(s)
else:
    print(s - dMin[s % D])
# 1==14432 verno
# 2==45978688 verno
