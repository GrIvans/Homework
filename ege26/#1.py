with open('26data/26-1.txt') as fin:
    data = fin.readlines()

s, _ = map(int, data[0].split())
del data[0]
data = sorted(list(map(int, data)))

total = 0
for i, val in enumerate(data):
    if total + val > s: break
    total += val
print(i)

delta = s - total
candidates = [x for x in data
if x - data[i - 1] <= delta]
print(max(candidates))
