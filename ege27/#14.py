#data = open('27data/14/27-14a.txt').readlines()
data = open('27data/14/27-14b.txt').readlines()
#data = open('input.txt').readlines()
# 1--17 верно
# 2--150016535 верно
n = int(data[0])
data = sorted(list(map(int, data[1:])), reverse=1)
kolvo = 0
i = 0
for i in range(n):
    for j in range(i + 1, n):
        r = data[i] + data[j]
        if r % 12 == 0:
            kolvo += 1
print(kolvo)
