a = [0] * 26
a[1] = 1

for i in range(1, 26):
    if i == 21:
        continue
    a[i] += a[i - 1]
    if (i - 1) % 2 == 0:
        a[i] += a[(i - 1) // 2]

for i, m in enumerate(a):
    print(i, m)
#ans==20 verno
