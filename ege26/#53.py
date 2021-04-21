f = open('26data/26-53.txt')
#f = open('test.txt')
chet = []
nechet = []
n = int(f.readline())
for i in range(n):
    temp = int(f.readline())
    if temp % 2 == 1:
        nechet.append(temp)
    else:
        chet.append(temp)
ans = []
for i in range(len(nechet) - 1):
    for j in range(i + 1, len(nechet)):
        sr = (nechet[i] + nechet[j]) // 2
        if sr % 2 == 0:
            if sr in chet:
                ans.append(sr)
        else:
            if sr in nechet:
                ans.append(sr)
print(len(ans), max(ans))
# 38 884877115
