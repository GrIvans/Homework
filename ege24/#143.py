stroka = open('24data/24-s1.txt').readlines()
ans = 0
for s in stroka: 
    k = 0
    for i in range(len(s) - 2):
        if s[i] == 'Z' and s[i + 2] == 'R' and s[i + 3] == 'O':
            k += 1
    if k > 0:
        ans += 1
print(ans)
