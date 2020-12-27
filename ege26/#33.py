data = open('26data/26-s1.txt').readlines()
#data = open('input.txt').readlines()
del data[0]
data = sorted(list(map(int, data)))
total = 0
skid = []
for i in data:
    if i > 200:
        skid.append(i)
    else:
        total += i
print(skid[len(skid) // 2 - 1])
for i in range(len(skid) // 2):
    skid[i] = skid[i] * 0.7
print(1 + int(sum(skid)) + total)
