data = open('27data/33/27-34a.txt')
#data = open('27data/33/27-34b.txt')
#data = open('input.txt')
D = 6
n = int(data.readline())
s, dMin = 0, [10001] * D
for i in range(n):
    a, b, c = map(int, data.readline().split())
    a, b, c = max(a, b, c), a + b + c - max(a, b, c) - min(a, b, c), min(a, b, c)