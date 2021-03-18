def f(i):
    a = 78
    s = ''
    while a != 0:
        s = str(a % i) + s
        a //= i
    return s


def prav(i):
    s = f(i)
    for i in range(1, len(s)):
        if int(s[i - 1]) % 2 == int(s[i]) % 2:
            return False
    return True


ans = 0
for i in range(2, 11):
    if prav(i):
        ans += i
    print(i, f(i))
print(ans)

