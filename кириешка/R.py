s = open('input.txt', encoding='utf-8').readlines()
ansvers = []
for i in s:
    x = i.split()
    ball = int(x[-1])
    ansvers.append((x[0] + ' ' + x[1], ball))
mx = 0
mx2 = 0
for i in ansvers:
    score = i[1]
    if score > mx:
        mx2 = mx
        mx = score
    elif score > mx2 and score != mx:
        mx2 = score
k = 0
ans = ''
for n in ansvers:
    if n[1] == mx2:
        ans = n[0]
        k += 1
if k == 1:
    print(ans)
else:
    print(k)
