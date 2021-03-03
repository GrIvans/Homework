a = [0] * 21
a[1] = 1

for i in range(2, 21):
    a[i] += a[i - 1]
    if i % (3 / 2) == 0:
        a[i] += a[i // 3 + (i // 3)]

for i, m in enumerate(a):
    print(i, m)
# ans==32 verno
