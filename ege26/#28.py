data = open('input.txt').readlines()
s, _ = map(int, data[0].split())
del data[0]
data = sorted(list(map(int, data)), reverse=1)

total = 0
k = 0