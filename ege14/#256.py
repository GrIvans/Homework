def f(i):
    a = 2345
    s = ''
    while a != 0:
        s = str(a % i) + s
        a //= i
    return sum(map(int, s))


mx = 0
for i in range(2, 11):
    print(i, f(i))
#ans--7
