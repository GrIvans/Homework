def f(n):
    if n <= 3:
        return n
    elif n > 3 and n % 2 == 0:
        return 2 * n * n + f(n - 1)
    elif n > 3 and n % 2 == 1:
        return n * n * n + n + f(n - 1)


k = 0
for i in range(1, 1000):
    if f(i) < 10**7:
        k += 1
print(k)
