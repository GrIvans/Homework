#data_inp = open('27data/20/27-20a.txt').readlines()
#data_inp = open('27data/20/27-20b.txt').readlines()
data_inp = open('input.txt').readlines()

kolvo = int(data_inp[0])
data = []
data_inp = data_inp[1:]
for i in range(kolvo):
    a, b = map(int, data_inp[i].split())
    data.append([a, b])
mx_dlin = 0
    
print(mx_dlin)

