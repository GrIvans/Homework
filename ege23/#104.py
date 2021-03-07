a = []

b = 3
c = 22
n = 7

for i in range(n + 1):
    a.append([0] * 32 * 4)

a[0][b] = 1
for i in range(n):
    for j in range(c):
        a[i + 1][j + 1] += a[i][j]
        a[i + 1][j + 3] += a[i][j]
        a[i + 1][j + 3] += a[i][j]
print(a[n][c])
