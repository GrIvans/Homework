a = 25**94 + 5**216 - 125
k = 0
while a != 0:
    if a % 5 == 4:
        k += 1
    a //= 5
print(k)
