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
                m = (i, a // i)
    return m


ans = ()
mn = 100001
k = 0
for i in range(309829, 365875):
    s = delit(i)
    if s != ():
        k += 1
        if s[1] - s[0] < mn:
            mn = s[1] - s[0]
            ans = s
print(ans)
