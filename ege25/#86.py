def f(a):
    n = (a**.5)
    k = 0
    for i in range(2, int(n) + 1):
        if a % i == 0:
            k += 1
            if a // i != i:
                k += 1
    return k


sm = 0
for i in range(4986, 32599 + 1):
    if f(i) == 2:
        sm += i
print(sm)
