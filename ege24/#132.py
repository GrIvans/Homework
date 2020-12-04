s = open('24data/24-J1.txt', 'r').read()

k = 0
mx = 0
s = s.replace('КОТ', '1')
ans = []
for i in s:
    if i == '1':
        k += 1
    else:
        mx = max(k, mx)
        k = 0
print(max(mx, k))
