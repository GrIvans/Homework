a = [0] * 17
a[2] = 1

for i in range(3, 17):
    a[i] += a[i - 1]
    if i % 2 == 0:
        a[i] += a[i // 2]
    if (i - 1) % 2 == 0:
        a[i] += a[(i - 1) // 2]
for i, m in enumerate(a):
    print(i, m)
# ans== 40 verno
