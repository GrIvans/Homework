a = [0] * 52
a[25] = 1

for i in range(26, 52):
    a[i] += a[i - 1]
    if i % 10 < 9:
        a[i] += a[i - 11]
    else:
        a[i] += a[i - 10]

for i, m in enumerate(a):
    print(i, m)
# ans==33 verno
