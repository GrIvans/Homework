a = 4 * 125**4 - 25**4 + 9
k = 0
while a != 0:
    if a % 5 == 4:
        k += 1
    a //= 5
print(k)
