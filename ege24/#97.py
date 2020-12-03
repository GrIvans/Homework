s = open('24data/24-4.txt').read()

k = 0
mx = 0
st = ''
for i in range(len(s) - 1):
    if s[i] < s[i + 1] and s[i].isalpha() and s[i + 1].isalpha(): 
        k += 1
    else:
        mx = max(k + 1, mx)
        k = 0
print(max(k + 1, mx))
