s = open('24data/24-1.txt').read()

mx = 0
k = ''

for i in s:
    if i.isdigit():
        if int(i) % 2 == 0:
            k += i
        else:
            fl = True
            if k != '':
                fl = True
                for n in k:
                    if int(n) % 2 == 1:
                        fl = False
                if fl:
                    mx = max(int(k), mx)
            k = ''
    else:
        if k != '':
            fl = True
            for n in k:
                if int(n) % 2 == 1:
                    fl = False
            if fl:
                mx = max(int(k), mx)
        k = ''
print(mx)
