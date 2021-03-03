a = [0] * 23
a[3] = 1

for i in range(4, 23):
    a[i] += a[i - 1]
    a[i] += a[i - 2]
    a[i] += a[i - 3]

print(a[22])