def delit(a):
    n = int(a**0.5)
    m = [1]
    for i in range(2, n + 1):
        if a % i == 0:
            m.append(i)
            if a // i != i:
                m.append(a // i)
    return m


# неверно
print(delit)
for i in range(300, 351):
    a = delit(i)
    n = sum(a)
    if n == i:
        print(i)
