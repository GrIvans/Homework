#data = open('27data/12/27-12a.txt')
#data = open('27data/12/27-12b.txt')
data = open('input.txt').readlines()

data = data[1:]
data = list(map(int, data))

for i in range(len(data)):
    