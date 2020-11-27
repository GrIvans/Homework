text = open('input.txt', encoding='utf-8').readlines()
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

if kol_mest != 450:
    num = 450 - kol_mest
    while i in sorted(parties, key=lambda x: parties.get(x)[1], reverse=1) and num != 0:
        parties[i][0] += 1
        num -= 1

for l in (parties):
    print(str(l) + ' ' + str(parties[l][0]))
