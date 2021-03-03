a = [0] * 23
a[2] = 1

for i in range(3, 23):
    a[i] += a[i - 1]
    a[i] += a[i - 3]
    a[i] += a[i // 3]
for i, m in enumerate((a)):
    print(i, m)
#ans==2196 verno
