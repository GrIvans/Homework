x = 49**12 - 7**10 + 7**8 - 49
k = 0
while x != 0:
    if x % 7 == 6:
        k += 1
    x //= 7
print(k)
