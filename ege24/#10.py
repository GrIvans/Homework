s = open('24data/k7-45.txt').read()
mx_c = 0
k = 0
for i in s:
    if i == 'C':
        k += 1
    else:
        mx_c = max(mx_c, k)
        k = 0
print(max(mx_c, k))