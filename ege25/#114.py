def prost(a):
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            return False
    return True


def delit(a):
    m = ()
    for i in range(2, int(a**.5) + 1):
        if a % i == 0 and i != a // i:
            if prost(i) and prost(a // i):
                return((i, a // i))
    return ()


mx = 0
ans = ()
for i in range(326359, 421987):
    s = delit(i)
    if s != ():
        if s[1] - s[0] > mx:
            mx = s[1] - s[0]
            ans = s
print(ans)
