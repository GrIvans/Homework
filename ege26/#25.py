data = open('26data/26-k5.txt').readlines()
_, k, m = map(int, data[0].split())
del data[0]
data = sorted(list(map(int, data)))
print(data[-m])
ans = []
for i, cost in enumerate(data):
    if i in range(0, k):
        ans.append(cost)
print(int((sum(ans) / len(ans))))
