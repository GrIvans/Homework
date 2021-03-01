def f(k):
    a = [0] * 81
    a[k] = 1
    for i in range(k + 1, 81):
        a[i] += a[i - 1]
        a[i] += a[i % 4]
        if i % 2 == 0:
            a[i] += a[i // 2]
    print(k, a[80])
    return a[80]


k = 0
for j in range(1, 80):
    if f(j) <= 5:
        k += 1
print(k)
