def f(a):
    s = ''
    while a != 0:
        s = str(a % 3) + s
        a //= 3
    return s


for i in range(1, 21):
    if f(i)[0] =='2':
        print(i)