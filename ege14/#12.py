def f(a):
    k = 0
    while a != 0:
        if a % 6 == 3:
            k += 1
        a //= 6
    return k

k = 0
for i in range(19, 34):
    if f(i) > 0:
        k += f(i)
print(k)
