a = []

b = 1  # начальное значение
c = 34  # конечное значение
n = 8  # количество шагов
for i in range(n + 1):
    a.append([0] * 34 * 4)

a[0][b] = 1
for i in range(n):
    for j in range(c):
        a[i + 1][j + 1] += a[i][j]
        a[i + 1][j * 2] += a[i][j]
        a[i + 1][j * 3] += a[i][j]

print(a[n][c])
