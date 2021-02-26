data = open('27data/32/27-32a.txt')
#data = open('27data/32/27-32b.txt')
#data = open('input.txt')
n = int(data.readline())
D = 11
s, dMin = 0, [10001] * D
for i in range(n):
    a, b, c = map(int, data.readline().split())
    a, b, c = max(a, b, c), a + b + c - max(a, b, c) - \
        min(a, b, c), min(a, b, c)
    s += c
    d = min(abs(c - b), abs(a - c))
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
    print(s + dMin[D - (s % D)])
#1==5896 verno 
#2==14078757 verno
