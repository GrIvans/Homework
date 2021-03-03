def f(a):
    for i in range(a - 1):
        if i + i + 1 == a:
            return (True, i)
    return (False, -1)


a = [0] * 11
a[2] = 1

for i in range(3, 10):
    a[i] += a[i - 1]
    a[i] += a[i - 2]
    s = f(i)
    if s[0]:
        a[i] += a[s[1] + 1]

for i, m in enumerate(a):
    print(i, m)
# ans== 57 verno
