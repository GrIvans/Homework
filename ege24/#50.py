s = open('24data/k7-m25.txt').read()

alf = ['A', 'B', 'C', 'D', 'E', 'F']
k, num = 0, 0

for i in range(1, len(s) - 1):
    if alf.index(s[i]) > alf.index(s[i - 1]) and alf.index(s[i]) > alf.index(s[i + 1]):
        k += 1
        num = i - 1
print(k, num)