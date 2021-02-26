a = 9**20 + 3**60 - 5
k = 0
while a != 0:
    if a % 3 == 2:
        k += 1
    a //= 3
print(k)
