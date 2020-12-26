data = open('26data/26-s1.txt').readlines()
#data = open('input.txt').readlines()
del data[0]
data = list(map(int, data))
skid = []
total = 0
for i in data:
    if i > 100:
        skid.append(i)
    else:
        total += i
skid.sort()
max_skid = skid[len(skid) // 2 - len(skid) % 2]
for i in range(len(skid) // 2):
    skid[i] = skid[i] * 0.9
print(int(sum(skid)) + total + 1)
print(max_skid)
