s = open('24data/24-J3.txt').read()
s = s.replace('TIK', '1')
s = s.replace('TOK', '1')
print(s.count('1'))