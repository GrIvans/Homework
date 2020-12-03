s = open('24data/24-1.txt').read()

mx = 0
k = ''

for i in s:
    if i.isdigit():
        k += i
    else:
        if k != '':
            if int(k) % 2 == 1:
                mx = max(int(k), mx)
        k = ''
print(mx)