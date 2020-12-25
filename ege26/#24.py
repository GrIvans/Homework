data = open('26data/26-k4.txt').readlines()
#data = open('input.txt').readlines()
_, k = map(int, data[0].split())
del data[0]
data = sorted(list(map(int, data)), reverse=1)

otl = data[:k]
hor = data[k: k + k]
print(int(sum(hor) / len(hor)), int(sum(otl) / len(otl)))
