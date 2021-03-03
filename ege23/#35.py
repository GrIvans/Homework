a = [0] * 16
a[1] = 1

for i in range(2, 16):
    a[i] += a[i - 1]
    if i % 2 == 0:
        a[i] += a[i // 2]
    if (i - 1) % 2 == 0:
        a[i] += a[(i - 1) // 2]
    if i % 10 == 0:
        a[i] += a[i // 10]

for i, m in enumerate(a):
    print(i, m)
#ans== 84 verno
