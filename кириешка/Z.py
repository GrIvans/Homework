def f(x):
    i = x.split()
    school = int(i[2])
    return school


text = open('input.txt', encoding='utf-8').readlines()
text.sort(key=f)
ansv_dict = {}
for line in text:
    i = line.split()
    school = int(i[2])
    ansv_dict[school] = ansv_dict.get(school, 0) + 1
ansvers = sorted(ansv_dict, key=lambda x: ansv_dict.get(x), reverse=1)
print(*ansvers)
