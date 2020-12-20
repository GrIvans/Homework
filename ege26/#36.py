s = open('26data/26-j8.txt').read().split()
n = int(s[0])
s.pop(0)
a = []
for i in range(n):
    a.append(int(s[i]))

skid_1 = sorted(a)
skid_2 = skid_1
n1 = int(n * 0.7)
n2 = int(n * 0.5)
for i in range(n1 + 1):
    skid_1[i] = skid_1[i] * 0.7

for i in range(n1 + 1, n):
    skid_1[i] = skid_1[i] * 0.6

for i in range(n2 + 1):
    skid_2[i] = skid_2[i] * 0.6

for i in range(n2, n):
    skid_2[i] = skid_2[i] * 0.65
print(sum(skid_2))