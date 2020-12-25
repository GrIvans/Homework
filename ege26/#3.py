data = open('26data/26-3.txt').readlines()

s, _ = map(int, data[0].split())
del data[0]
data = sorted(list(map(int, data)))

total = 0
for i, val in enumerate(data):
    if total + val > s: break
    total += val
print(i)

delta = s - total
condidates = [x for x in data
if x - data[i - 1] <= delta]
print(max(condidates))