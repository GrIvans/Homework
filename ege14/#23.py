def f(i):
    s = ''
    while i != 0:
        s = str(i % 5) + s
        i //= 5
    if s == '1234':
        return True
    return False


for i in range(1, 1000):
    if f(i):
        print(i)
#ans--194