s = open('24data/24-1.txt').read()

k = 1
mx = 0
imx = 0
p = 0
for i in range(len(s) - 1):
    if s[i] < s[i + 1]: 
        k += 1
    else:
        if k > mx:
            mx = k
            imx = p
        k = 1
        p = i
if k > mx:
    imx = p
    mx = k
print(imx + 1)
