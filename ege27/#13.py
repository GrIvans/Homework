data = open('27data/13/27-13a.txt').readlines()
#data = open('27data/13/27-13b.txt').readlines()
#data = open('input.txt').readlines()
#1--30 верно
#2--
n = int(data[0])

data = list(map(int, data[1:]))
elem = []
for i in range(n):
    for j in range(i + 7, n):
        r = data[i] * data[j]
        if r % 14 == 0:
            elem.append((data[i], data[j]))
print(len(elem))
