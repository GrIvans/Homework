s = open('input.txt', encoding='utf-8').readlines()
out = []
ansv_dict = {}
summa_ballov = 0
kol = len(s)
for i in s:
    i = i.split()
    school = int(i[2])
    score = int(i[3])
    summa_ballov += score
    if school not in ansv_dict:
        ansv_dict[school] =[]
    ansv_dict[school].append(score)
sredniy_ball = summa_ballov / kol
for i in ansv_dict:
    sum_ball_school = 0
    kol_uchenikov = len(ansv_dict[i])
    for n in ansv_dict[i]:
        sum_ball_school += n
    sred_ball_school = sum_ball_school / kol_uchenikov
    if sred_ball_school > sredniy_ball:
        out.append(i)
print(*(sorted(out)))
