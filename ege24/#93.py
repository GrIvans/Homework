s = open('input.txt').read()

k = 0
st = ''
for i in range(len(s) - 1):
    if ord(s[i]) < ord(s[i + 1]):
        k += 1
print()
