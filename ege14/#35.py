def f(a):
    k = 0
    while a != 0:
        if a % 4 == 3:
            k += 1
        a //= 4
    return k


k = 0
for i in range(13, 24):
    k += f(i)
print(k)