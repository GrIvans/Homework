s = open('24data/k7-m21.txt').read()
slovar = ['A', 'B', 'C', 'D', 'E', 'F']
k = 0
lst = 0
for i in range(len(s) - 2):
    if slovar.index(s[i]) < slovar.index(s[i + 1]) < slovar.index(s[i + 2]):
        k += 1
        lst = i
print(k, lst)
