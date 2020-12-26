data = open('input.txt').readlines()
del data[0]
data = list(map(int, data))
skid = [max(data)]
data.remove(max(data))
total = 0

