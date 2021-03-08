a = (7**(80) - 7**4) * 5 / 6 * 8
k = 0
while a != 0:
    if a % 7 == 4:
        k += 1
    a //= 7
print(k)
#neverno