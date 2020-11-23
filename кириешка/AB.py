def f(i):
    x = i.split()
    return int(x[-2])

text = open('input.txt', encoding='utf-8').readlines()
text.sort(key=f)
schools = {}
mx_ball = 0
for line in text:
    sim = line.split()
    schol = int(sim[-2])
    ball = int(sim[-1])
    if schol not in schools:
        schools[schol] = []
    schools[schol].append(ball)
    mx_ball = max(mx_ball, ball)

for school in schools:
    mx_kol = 0
    for i in schools[school]:
        if i == mx_ball:
            mx_kol += 1
    schools[school] = mx_kol
anv = sorted(schools, key=schools.get, reverse=1)
mx_school = schools[anv[0]]
for i in anv:
    if mx_school == schools[i]:
        print(i, end=' ')
