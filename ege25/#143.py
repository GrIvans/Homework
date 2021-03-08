def prost(a):
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            return False
    return True


for i in range(33333, 55556):
    if prost(i):
        s = sum(map(int, str(i)))
        if s > 35:
            print(i, s)
