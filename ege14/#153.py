a = 2 * 27**7 + 3**10 - 9
k = 0
while a != 0:
    if a % 3 == 0:
        k += 1
    a //= 3
print(k)
