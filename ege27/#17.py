data = open('27data/17/27-17a.txt').readlines()
data = open('27data/17/27-17b.txt').readlines()
#data = open('input.txt').readlines()
#1--6
#2--129920689
n = int(data[0])
data = list(map(int, data[1:]))
kolvo = 0

for i in range(n):
    for j in range(i + 5, n):
        if (data[i] + data[j]) % 2 == 1 and (data[i] * data[j]) % 13 == 0:
            kolvo += 1
print(kolvo)
