def f(a):
    if a == 1:
        return False
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            return False
    return True

k = 1
for i in range(2943444, 2943529 + 1):
    if f(i):
        print(k, i)
        k += 1
