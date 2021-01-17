def deletel(a):
    chet = []
    nechet = []
    n = int(a**.5)
    for i in range(2, n + 1):
        if a % i == 0:
            if i % 2 == 0:
                chet.append(i)
            else:
                nechet.append(a // i)
            if a // i != i:
                if i % 2 == 0:
                    chet.append(i)
                else:
                    nechet.append(a // i)
    if len(chet) > 70 and len(nechet) > 70 and len(chet) == len(nechet):
        for i in sorted(chet + nechet):
            if i > 1000:
                mn = i
            return (True, a, mn)
    return (False, 0, 0)


for i in range(326496, 649632 + 1):
    a = deletel(i)
    if a[0]:
        print(a)
