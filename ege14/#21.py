def f(a):
    s = ''
    while a != 0:
        s = str(a % 6) + s
        a //= 6
    return (s)


for i in range(1, 26):
    if int(f(i)[0]) == 4:
        print(i)
