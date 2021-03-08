def f(n):
    if n <= 3:
        return 1
    if n in range(4, 33):
        return (n // 4) + f(n - 3)
    if n > 32:
        return 2 * f(n - 5)


print(f(100))
