data = open('27data/15/27-15a.txt').readlines()
data = open('27data/15/27-15b.txt').readlines()
#data = open('input.txt').readlines()
#1--8
#2--128567918
n = int(data[0])
data = list(map(int, data[1:]))
kolvo = 0
for i in range(n):
    for j in range(i + 5, n):
        r = data[i] + data[j]
        if r % 14 == 0:
            kolvo += 1
print(kolvo)
