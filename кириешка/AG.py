s = open('input.txt', encoding='utf-8').readlines()
kol_zachisleniy = int(s[0])
s.pop(0)
ucheniki = []
for i in s:
    x = i.split()
    eg_1 = int(x[-1])
    eg_2 = int(x[-2])
    eg_3 = int(x[-3])
    sm = eg_1 + eg_2 + eg_3
    if eg_1 > 40 and eg_2 > 40 and eg_3 > 40:
        ucheniki.append((i, sm))
ucheniki.sort(key=lambda x: x[1] , reverse=1)
dlina_uchenik = len(ucheniki)

print(ucheniki)

if dlina_uchenik == 0:
    print(0)
elif dlina_uchenik <= kol_zachisleniy:
    print(1)
elif dlina_uchenik > kol_zachisleniy:
    proh_ball = ucheniki[kol_zachisleniy - 1][1]
    if proh_ball > ucheniki[kol_zachisleniy][1]:
        print(ucheniki[kol_zachisleniy - 1][1])
    else:
        for n in range(kol_zachisleniy):
            if proh_ball == ucheniki[n][1]:
                if n == 1:
                    print(ucheniki[0][1])
                    break
                else:
                    print(ucheniki[n - 1][1])
                    break
