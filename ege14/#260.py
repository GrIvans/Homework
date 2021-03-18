def sis(i):
    a = 609
    s = ''
    while a != 0:
        s = str(a % i) + s
        a //= i
    return s


def prav(i):
    s = sis(i)
    if int(s[0]) % 2 != int(s[-1]) % 2:
        return True
    return False


ans = 0
for i in range(2, 11):
    if prav(i):
        ans += i
print(ans)
