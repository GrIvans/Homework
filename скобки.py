s = open('input1.txt', encoding='utf-8').read()
for i in range(len(s)):
    p = s.find('(')
    if p != -1:
        p1 = s.rfind(')')
        if p1 > p and p1 != -1:
            s = s.replace('(', '', 1)
            s = s.replace(')', '', 1)
    p = s.find('[')
    if p != -1:
        p1 = s.rfind(']')
        if p1 > p and p1 != -1:
            s = s.replace('[', '', 1)
            s = s.replace(']', '', 1)
    p = s.find('{')
    if p != -1:
        p1 = s.rfind('}')
        if p1 > p and p1 != -1:
            s = s.replace('{', '', 1)
            s = s.replace('}', '', 1)
if s == '':
    print('YES')
else:
    if s.find('(') != -1:
        print('Лишняя скобка -- "("')
    if s.find('(') != -1:
        print('Лишняя скобка -- ")"')
    if s.find('[') != -1:
        print('Лишняя скобка -- "["')
    if s.find(']') != -1:
        print('Лишняя скобка -- "]"')
    if s.find('{') != -1:
        print('Лишняя скобка -- "{"')
    if s.find('}') != -1:
        print('Лишняя скобка -- "}"')
