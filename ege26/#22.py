data = open('26data/26-k2.txt').readlines()
#data = open('input.txt').readlines()
_, k = map(int, data[0].split())
del data[0]
data = sorted(list(map(int, data)))
for i in range(k):
    del data[0]
    del data[-1]

print(data[-1])

print(int(sum(data) / len(data)))