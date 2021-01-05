#data = open('27data/16/27-16a.txt').readlines()
data = open('27data/16/27-16b.txt').readlines()
#data = open('input.txt').readlines()

# 1--19
# 2--132286186

kolvo = 0
n = int(data[0])
data = list(map(int, data[1:]))
for i in range(n):
    for j in range(i + 1, n):
        if (data[i] + data[j]) % 2 == 1 and (data[i] * data[j]) % 13 == 0:
            kolvo += 1
print(kolvo)
