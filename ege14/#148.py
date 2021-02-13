x = 27**4 - 9**5 + 3**8 - 25
k = 0
while x != 0:
    if x % 3 == 2:
        k += 1
    x //= 3
print(k)
