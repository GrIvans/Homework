a = [0] * 18
a[1] = 1
for i in range(2, 17):
    a[i] += a[i - 1]
    if i % 2 == 0:
        a[i] += a[i //2]
for i, m in enumerate(a):
    print(i, m)
#ans==36 verno