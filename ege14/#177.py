a = 9**7 + 3**8 - 1
d = {}
while a != 0:
    s = str(a % 3)
    d[s] = d.get(s, 0) + 1
    a //= 3
print(d[sorted(d, key=d.get)[-1]])
