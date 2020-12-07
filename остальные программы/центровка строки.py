s = open('input.txt', encoding='utf-8').readlines()
fout = open('output.txt', 'w', encoding='utf-8')
for i in s:
    stroka = i[:-1]
    if len(stroka) % 2 == 0:
        stroka = ' ' * ((20 - len(stroka)) // 2) + stroka + '\n'
        fout.write(stroka)  
    else:
        stroka = ' ' * (((20 - len(stroka) - 1) // 2)) + stroka + '\n'
        fout.write(stroka)
