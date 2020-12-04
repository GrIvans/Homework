s = open('24data/24-s1.txt').readlines()
k = 0
for i in s:
    if i.count('YZ') > 1:
        k += 1
print(k)