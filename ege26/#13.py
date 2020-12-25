data = open('26data/26-13.txt').readlines()
s, _ = map(int, data[0].split())
del data[0]
data = sorted(list(map(int, data)))

total = 0
for i, val in enumerate(data):
    if val + total > s: break
    total += val
print(i)

delta = s - total
con = [x for x in data
if x - data[i - 1] <= delta]
print(max(con))