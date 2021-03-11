s = open('24data/24-j9.txt').read() + '1'
k = 0
a = ''
for i in s:
    if len(a) != 5:
        a += i
    if len(a) % 5 == 0:
        if a == a[::-1]:
            k += 1
        a = ''
print(k)
