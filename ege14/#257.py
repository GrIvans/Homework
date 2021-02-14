def f(i):
    a = 3456
    s = ''
    while a != 0:
        if (a % i) % 2 == 1:
            return False
        a //= i
    return True

mx = 0
for i in range(2, 11):
    if f(i):
        print(i)
#ans--10
