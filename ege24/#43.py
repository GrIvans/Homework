s = open('24data/k7-m5.txt').read()

ansv = []
k = 0
ns = ''
for i in s:
    news = i
    if i == 'C':
        k += 1
        news = 'c'
    else:
        if k > 0:
            ansv.append(k)
        k = 0
    ns += news
if k != 0:
    ansv.append(k)
print(len(ansv))
print(s[:16], s[-15:])
stroka = ''
nomer = 0
for n in range(len(ns) - 1):
    if ns[n] != ns[n + 1] and ns[n + 1] == 'c':
        stroka += ns[n] + str(ansv[nomer]) 
        nomer += 1
    else:
        stroka += ns[n]
stroka += ns[-1]
print(stroka[:16], stroka[-15:])
