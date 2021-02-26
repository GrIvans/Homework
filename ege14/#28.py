def f(i):
    a = 144
    s = ''
    while a != 0:
        s = str(a % i) + s
        a //= i
    if s == '264':
        return True
    return False


for i in range(2, 100):
    if f(i):
        print(i)
