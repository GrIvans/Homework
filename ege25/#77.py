def prost(a):
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            return False
    return True


k = 0
for i in range(2, 20001):
    if prost(i):
        k += 1
print(k)
