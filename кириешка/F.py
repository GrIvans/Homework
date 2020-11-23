s = open('input.txt', 'r', encoding='utf-8').readlines()
fout = open('output.txt', 'w', encoding='utf-8')
s.sort(key=len, reverse=True)
mx = len(s[0])
for i in s:
    if len(i) == mx:
        fout.write(i)        

