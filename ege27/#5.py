data = open('27data/5/27-5a.txt')
#data = open('27data/5/27-5b.txt')
#data = open('input.txt')
D = 5
s, dMin = 0, [10001] * D
n = int(data.readline())
for i in range(n):
    a, b = map(int, data.readline().split())
    s += min(a, b)
    d = abs(a - b)
    r = d % D
    if r > 0:
        for k in range(1, D):
            dMinNew = dMin[:]
            r0 = (r + k) % D
            dMinNew[r0] = min(d + dMin[k], dMin[r0])
        dMinNew[r] = min(d, dMin[r])
        dMin = dMinNew[:]
if s % D == 0:
    print(s)
else:
    print(s + dMin[D - (s % D)])
# 1==75960 verno
# 2==203343860 verno
