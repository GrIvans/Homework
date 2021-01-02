data = open('27data/8/27-8a.txt')
#data = open('27data/8/27-8b.txt')
#data = open('input.txt')

kolvo = int(data.readline())
ans = []
izm = []
for i in range(kolvo):
    if len(izm) < 5:
        izm.append(int(data.readline()))
    else:
        ans.append(sorted(izm))
        izm = [int(data.readline())]
if len(izm) != 0:
    ans.append(sorted(izm))

ans.sort()
print(ans)
print(ans[0][0]**2 + ans[0][1]**2)
