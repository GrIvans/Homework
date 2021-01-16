def nechet(a):
    while a != 0:
        if (a % 10) % 2 == 0:
            return False
        a //= 10
    return True

#не работает
def sumCifr(a):
    sm = 0
    while a != 0:
        sm += a % 10
        a //= 10
    return sm


sm = 0
for i in range(3159, 31584 + 1):
    if nechet(i):
        sm += sumCifr(i)
print(sm)
