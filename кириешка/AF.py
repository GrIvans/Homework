def f(i):
    x = i.rfind(' ')
    return(i[:x])


text = open('input.txt', encoding='utf-8').readlines()
text.sort(key=f)
parties = {}
summa_ballov = 0
for line in text:
    x = line.split()
    i = line.rfind(' ')
    parti = line[:i]
    parties[parti] = parties.get(parti, 0) + int(x[-1])
    summa_ballov += int(x[-1])

izb_chislo = summa_ballov / 450

kol_mest = 0
for i in parties:
    mest = parties[i] / izb_chislo
    drob = mest - int(mest)
    parties[i] = [int(mest), drob]
    kol_mest += int(mest)

if kol_mest == 450:
    for i in sorted(parties, key=parties.get):
        print(i + ' ' + str(parties[i][0]))
else:
    num = 450 - kol_mest
    while i in sorted(parties, key=lambda x: parties.get(x)[1], reverse=0) and num != 0:
        m = []
        k = 0
        for n in parties[i]:
            m.append(n)
            k += 1
        m[0] += 1
        parties[i] = m 
        num -= 1

for l in sorted(parties, key=parties.get):
    print(str(l) + ' ' + str(parties[l][0]))