def f(a):
    n = int(a**.5)
    m = []
    for i in range(1, n + 1):
        m.append(i)
        if a // i != i:
            m.append(a // i)
    return m
#долго
ans = []
for i in range(2, 10000001):
    ans.append((len(f(i)), i))
d = []
for i in ans:
    if i[1] == ans[0][1]:
        d.append(i)
print(d[-1])
