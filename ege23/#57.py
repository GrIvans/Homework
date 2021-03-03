a = [0] * 31
a[3] = 1

for i in range(2, 21):
    if i == 12:
        continue
    a[i] += a[i - 1]
    if i % 2 == 0:
        a[i] += a[i // 2]

for i in range(20):
    a[i] = 0

for i in range(21, 31):
    a[i] += a[i - 1]
    if i % 2 == 0:
        a[i] += a[i // 2]

for i, m in enumerate(a):
    print(i, m)
# ans== 12 verno
