def prost(a):
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            return False
    return True


sm = 0
for i in range(1060, 18813 + 1):
    if prost(i):
        sm += i
print(sm)
