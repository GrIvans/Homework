s = open('24data/24-5.txt').read()
num = 0
for i in range(len(s) - 1):
    if s[i] == '(' and s[i + 1] ==')':
        num += 1
        if num == 10000:
            print(i + 1)
            break