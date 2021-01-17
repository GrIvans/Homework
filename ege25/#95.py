def neub(a):
    s = str(a)
    for i in range(len(s) - 1):
        if int(s[i]) > int(s[i + 1]):
            return False
    return True


sm = 0
for i in range(1395, 22717 + 1):
    if neub(i):
        sm += i
print(sm)
