def f(i):
    a = int('65', 8)
    s = ''
    while a != 0:
        s = str(a % i) + s
        a //= i
    return int(s)


for i in range(2, 100):
    if f(i) == 311:
        print(i)
