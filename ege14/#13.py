def f(a):
    k = 0
    while a != 0:
        if a % 5 == 1:
            k += 1
        a //= 5
    return k


k = 0
for i in range(12, 32):
    k += f(i)
print(k)
