#не работает
data = open('26data/26-J1.txt').readlines()
#data = open('input.txt').readlines()
del data[0]
data = sorted(list(map(int, data)))

kolvo = 0
for cost in (data):
    for val in (data):
        if cost + val == 100 and data.index(val) != data.index(cost):
            kolvo += 1
            data.remove(val)
            data.remove(cost)
            break
print(kolvo)
