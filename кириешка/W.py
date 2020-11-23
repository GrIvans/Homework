s = open('input.txt', encoding='utf-8').readlines()
ansv_dict = {}
for i in s:
    i = i.split()
    ball = int(i[3])
    school = int(i[2])
    if ball not in ansv_dict:
        ansv_dict[ball] = []
    ansv_dict[ball].append(school)
ans = sorted(ansv_dict, reverse=1)
print(*sorted(set(ansv_dict[ans[0]])))
