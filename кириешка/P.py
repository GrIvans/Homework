s = open('input.txt', encoding='utf-8').readlines()
fout = open('output.txt', 'w', encoding='utf-8')
ansver9 = 0
ansver10 = 0
ansver11 = 0
ansver9_mx = 0
ansver10_mx = 0
ansver11_mx = 0

for i in s:
    x = i.split()
    chislo = int(x[-1])
    if x[-2] == '9':
        if ansver9_mx < chislo:
            ansver9 = ansver9_mx
            ansver9_mx = chislo
        elif chislo > ansver9 and chislo != ansver9_mx:
            ansver9 = chislo
    elif x[-2] == '10':
        if ansver10_mx < chislo:
            ansver10 = ansver10_mx
            ansver10_mx = chislo
        elif chislo > ansver10 and chislo != ansver10_mx:
            ansver10 = chislo
    elif x[-2] == '11':
        if ansver11_mx < chislo:
            ansver11 = ansver11_mx
            ansver11_mx = chislo
        elif chislo > ansver11 and chislo != ansver11_mx:
            ansver11 = chislo
print(ansver9, ansver10, ansver11)