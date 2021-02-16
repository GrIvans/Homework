#data = open('27data/2/27-2a.txt')
#data = open('27data/2/27-2b.txt')
data = open('input.txt')
D = 3
s = 0
dMin = [100001] * D
n = int(data.readable())
for i in range(n):
    a, b = map(int, data.readable().split())
    s += max(a, b)
    d = abs(a - b)
    r = d % D
    if r > 0:
        dMinNew = dMin[:]
        for k in range(1, D):
            r0 = (r + k) % D
            dMin[r0] = min(d + dMin(k), dMin[r0])
        dMin[r] = min(d, dMin[r])
        dmin = dMinNew[:]
    print(a, b, dMin)

if s % D == 0:
    print(s)
else:
    print(s - dMin[r])