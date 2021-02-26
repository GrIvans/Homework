a = 4 * 25**4 - 5**4 + 14
s = ''
while a != 0:
    s = str(a % 5) + s
    a //= 5
print(sum(map(int, s)))
