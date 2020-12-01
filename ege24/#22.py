s = open('24data/k7a-2.txt').read()

k = 0
mx_kol = 0
for i in s:
    if i == 'A' or i == 'C' or i == 'D':
        k += 1
    else:
        mx_kol = max(mx_kol, k)
        k = 0
print(max(mx_kol, k))
