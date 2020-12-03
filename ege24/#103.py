s = open('24data/24.txt').read()

k = 0
mx = 0
imx = 0
for i in range(len(s) - 1):
    if s[i] < s[i + 1] and s[i + 1].isalpha(): 
        k += 1
    else:
        if k + 1 > mx:
            mx = k + 1
            imx = i - k + 1
        k = 0
print(imx)
