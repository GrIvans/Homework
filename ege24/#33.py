s = open('24data/k7c-1.txt').read()
k = 0
mx_k = 0
perv = ['B', 'C', 'D']
vtor = ['B', 'D', 'E']
tret = ['B', 'C', 'E']

for i in range(len(s) - 1):
    if (s[i] in perv) and\
         (s[i + 1] in vtor and s[i + 1] != s[i]) \
             and (s[i + 2] in tret and s[i + 2] != s[i + 1]):
        k += 1
print(k)
