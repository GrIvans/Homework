a = open('26data/26-J1.txt').readlines()
n = int(a[0])
k = 0
for i in range(1, n - 1):
    for j in range(i + 1, n):
        if int(a[i]) + int(a[j]) == 100:
            a[i], a[j] = 0, 0
            k += 1
print(k)
