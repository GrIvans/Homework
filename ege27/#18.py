#не работает
#data = open('27data/18/27-18a.txt').readlines()
#data = open('27data/18/27-18.txt').readlines()
data = open('input.txt').readlines()
n = int(data[0])
data = list(map(int, data[1:]))
for i in range(5):
    data.append(0)
kolvo = 0
for i in range(n):
    for j in range(i + 1, i + 4):
        if (data[i] + data[j]) % 2 == 1 and (data[i] * data[j]) % 13 == 0:
            kolvo += 1
print(kolvo)
