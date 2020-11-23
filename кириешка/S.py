s = open('input.txt', encoding='utf-8').readlines()
ansv_dict = {}
mx = 0
for i in s:
    i = i.split()
    ansv_dict[int(i[2])] = ansv_dict.get(int(i[2]), 0) + 1
ansver = sorted(ansv_dict, key=lambda x: ansv_dict.get(x), reverse=True)
mx = ansv_dict[ansver[0]]
ans = []
for n in ansver:
    if mx == ansv_dict[n]:
        ans.append(n)
for i in sorted(ans):
    print(i, end=' ')
