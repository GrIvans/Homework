a = 49**13 + 7**33 - 49
k = 0
while a != 0:
    if a % 7 == 6:
        k += 1
    a //= 7
print(k)
