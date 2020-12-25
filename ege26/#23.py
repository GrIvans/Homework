data = open('26data/26-k3.txt').readlines()
#data = open('input.txt').readlines()
_, k, m = map(int, data[0].split())
del data[0]
data = sorted(list(map(int, data)), reverse=1)

print(data[k + m - 1])
print(data[k - 1])
