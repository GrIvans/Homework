def deletel(a):
    chet = []
    nechet = []
    n = int(a**.5)
    for i in range(1, n + 1):
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
    return chet, nechet


for i in range(326496, 649633):
    a, b = deletel(i)
    if len(b) >= 70 and len(a) == len(b):
        c = a + b
        for j in c:
            if j > 1000:
                mn = j
                break
        print(i, mn)
