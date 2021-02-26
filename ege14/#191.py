a = 125 + 25**3 + 5**9
k = 0
while a != 0:
    if a % 5 == 0:
        k += 1
    a //= 5
print(k)
