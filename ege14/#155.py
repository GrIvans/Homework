a = 9**8 + 3**5 - 2
k = 0
while a != 0:
    if a % 3 == 2:
        k += 1
    a //= 5
print(k)
