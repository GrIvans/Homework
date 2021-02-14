a = 9**5 + 3**25 - 20
s = ''
while a != 0:
    s = str(a % 3) + s
    a //= 3
print(sum(map(int, s)))