s = open('24data/24-j9.txt').read()
k = 0
for i in range(len(s) // 2):
    if s[i] == s[-i - 1]:
        k += 1
print(k)
#ans == 19351 verno