def f(n):
    if n <= 1:
        return n
    elif n > 1 and n % 2 == 0:
        return 1 + f(n // 2)
    elif n > 1 and n % 2 == 1:
        return 1 + f(n + 2)


for i in range(100):
    if f(i) == 16:
        print(i)
        break
