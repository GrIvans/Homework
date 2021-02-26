a = 9**8 + 3**25 - 14
s = ''
while a != 0:
    s = str(a % 3) + s
    a //= 3
print(sum(map(int, s)))
