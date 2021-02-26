a = 9**17 + 3**16 - 27
d = {}
while a != 0:
    s = str(a % 3)
    d[s] = d.get(s, 0) + 1
    a //= 3
print(d[sorted(d, key=d.get)[-1]])
