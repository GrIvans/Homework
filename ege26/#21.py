data = open('26data/26-k1.txt').readlines()
_, k = map(int, data[0].split())
del data[0]
data = sorted(list(map(int, data)), reverse=1)
sm = 0
for i, val in enumerate(data):
    if i != k - 1:
        sm += val * 0.2
    if i == k:
        print(val)
        break
print(int(sm))
