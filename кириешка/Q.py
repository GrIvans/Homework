s = open('input.txt', encoding='utf-8').readlines()
ansvers_dict = {}
for i in (s):
    i = i.split()
    ansvers_dict[int(i[3])] = ansvers_dict.get(int(i[3]), 0) + 1
mx = sorted(ansvers_dict, reverse=1)[0]
for i in sorted(ansvers_dict, reverse=1):
    if len(ansvers_dict) == 1:
        print(0)
    if i != mx:
        print(i, ansvers_dict[i])
        break
