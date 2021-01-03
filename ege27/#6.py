#data = open('27data/6/27-6a.txt').readlines()
data = open('27data/6/27-6b.txt').readlines()
#data = open('input.txt').readlines()
#1--782040 верно
#2--
kolvo = int(data[0])
data = data[1:]
data = sorted(list(map(int, data)), reverse=1)
r = []
for i in range(len(data)):
    for n in range(i + 1, len(data)):
        R = (data[i] * data[n])
        if R % 6 == 0:
            r.append(R)
print(sorted(r, reverse=1)[0])
