def prost(a):
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            return False
    return True


for i in range(2948, 20194 + 1):
    if prost(i):
        mx = i
print(mx)
