def drug(a):
    n = int(a**.5)
    m = [1]
    for i in range(2, n + 1):
        if a % i == 0:
            m.append(i)
            if a // i != i:
                m.append(a // i)
    return m

#неверно
for i in range(2, 30001):
    a = drug(i)
    b = drug(sum(a))
    if sum(b) == i and sum(a) == sum(b):
        print(sum(b), sum(a))
