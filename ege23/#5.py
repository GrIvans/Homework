a = [0] * 27
a[1] = 1

for i in range(2, 26):
    a[i] += a[i - 1]
    if i % 3 == 0:
        a[i] += a[i // 3]
    if i % 4 == 0:
        a[i] += a[i // 4]

for i, m in enumerate(a):
    print(i, m)
