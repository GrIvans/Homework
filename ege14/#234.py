a = 5 * 6561**46 + 5 * 729**15 - 5 * 5832 - 5
k = 0
while a != 0:
    if a % 9 == 4:
        k += 1
    a //= 9
print(k)
# ans==4 verno
