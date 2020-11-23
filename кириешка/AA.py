def f(x):
    i = x.split()
    return int(i[2])
text = open('input.txt', encoding='utf-8').readlines()
text.sort(key=f)
schools = {}
for i in text:
    x = i.split()
    school = int(x[-2])
    ball = int(x[-1])
    if school not in schools:
        schools[school] = []
    schools[school].append(ball)

for i in schools:
    kol = len(schools[i])
    summa = sum(schools[i])
    schools[i] = summa / kol

for i in sorted(schools, key=schools.get, reverse=1):
    print(i, end=' ')
