s = open('24data/24-1.txt').read()

mn = 9999999
k = ''

for i in s:
    if i.isdigit():
        k += i
    else:
        if k != '':
            if int(k) % 2 == 1:
                mn = min(int(k), mn)
        k = ''
print(mn)