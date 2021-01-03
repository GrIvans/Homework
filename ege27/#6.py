data = open('27data/6/27-6a.txt').readlines()
#data = open('27data/6/27-6b.txt').readlines()
#data = open('input.txt').readlines()
# 1--782040 верно
# 2--997002 верно
kolvo = int(data[0])
data = data[1:]
data = sorted(list(map(int, data)), reverse=1)
rmax = 0
left_gran = len(data)
i = 0
while i <= left_gran:
    n = i + 1
    while n <= left_gran:
        R = data[i] * data[n]
        if R % 6 == 0:
            rmax = max(rmax, R)
            left_gran = n
        n += 1
    i += 1
print(rmax)
