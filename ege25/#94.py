def prost(a):
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            return False
    return True


def summaCifr(a):
    sm = 0
    while a != 0:
        sm += a % 10
        a //= 10
    return sm


sm = 0
for i in range(3159, 31584 + 1):
    if prost(i):
        sm += summaCifr(i)
print(sm)
